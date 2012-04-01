from __future__ import division

from fluidsynth import fluidsynth

from lye.ast import MEASURE, PARTIAL, Music, Note, SciNote, Rest
from lye.grammar import Chord, LyeGrammar
from lye.instruments import NEAREST, fit
from lye.visitor import simplify_ast

class Melody(object):

    instrument = None
    volume = 127
    pan = 63

    def __init__(self, music, tpb):
        self.music = music
        self.tpb = tpb

    def __nonzero__(self):
        return any(self.music)

    def __repr__(self):
        return "Melody(%r, %d)" % (self.music, self.tpb)

    __str__ = __repr__

    def __mul__(self, value):
        """
        Extend this melody.
        """

        other = Melody(self.music, self.tpb)
        other.music.exprs *= value
        other.pan = self.pan
        other.volume = self.volume
        other.instrument = self.instrument
        return other

    def fit(self, strategy=NEAREST):
        """
        Force this melody to be within the range of its instrument.
        """

        if self.instrument:
            fit(self.music, self.instrument, strategy)

    def split(self):
        """
        Split this melody into harmonies.

        The melody should be harmonized somewhat already.

        Attempts are made to put as much work into the top of the melody as
        possible.

        Returned melodies are high-to-low.
        """

        count = 0

        for expr in self.music.exprs:
            if isinstance(expr, Chord):
                count = max(count, len(expr.notes))

        melodies = [Music([]) for i in range(count)]

        for expr in self.music.exprs:
            if isinstance(expr, Chord):
                for i, note in enumerate(sorted(expr.notes, reverse=True)):
                    melodies[i].exprs.append(note)
                for i in range(i + 1, len(melodies)):
                    # Create rests. Rely on the leaked note name from the
                    # previous loop.
                    melodies[i].exprs.append(Rest(note.duration))
            else:
                for melody in melodies:
                    melody.exprs.append(expr)

        rv = []
        for m in melodies:
            melody = Melody(m, self.tpb)
            melody.pan = self.pan
            melody.volume = self.volume
            rv.append(melody)
        return rv

    def schedule_notes(self):
        """
        Attach correct beginning times to notes.

        Additionally, this step discards rests.
        """

        relative_marker = 0
        partial = False
        partial_offset = 0
        scheduled = []

        for i, note in enumerate(self.notes):
            if isinstance(note, list):
                nested = Melody(note, self.tpb).schedule_notes()
                nested = [n._replace(begin=n.begin + relative_marker)
                    for n in nested]
                # If the next thing's not part of a voice, bump the relative
                # marker.
                if (len(self.notes) > i + 1 and
                    not isinstance(self.notes[i + 1], list)):
                        relative_marker = (nested[-1].begin +
                            nested[-1].duration)
                scheduled.extend(nested)

            elif note is MEASURE:
                remainder = ((relative_marker - partial_offset) % self.tpb)
                if remainder and not partial:
                    print "Marker is off by %d" % remainder
                # Start the next bar.
                partial = False
                partial_offset = remainder

            elif note is PARTIAL:
                partial = True

            elif isinstance(note, Chord):
                begin = relative_marker
                relative_marker = begin + note.duration

                for pitch in note.pitches:
                    scheduled.append(Note(pitch, begin, note.duration))

            elif isinstance(note, SciNote):
                # Note
                begin = relative_marker
                # XXX fudge?
                relative_marker = begin + note.duration

                scheduled.append(note._replace(begin=begin))

            elif isinstance(note, Rest):
                begin = relative_marker
                relative_marker = begin + note.duration

        return scheduled

    def to_fs(self, sequencer):
        """
        Sends the melody to `sequencer`.
        """

        scheduled = self.schedule_notes()

        # XXX
        # tpb = sequencer.ticks_per_beat
        # Each item in the seq is (fluidsynth.FS, (dest, destname))
        # We just want the dest
        dest = sequencer.items()[0][1][0]
        # XXX this fudge value might not be needed?
        ticks = sequencer.ticks + 10

        for pitch, begin, duration in scheduled:
            event = fluidsynth.FluidEvent()
            event.dest = dest
            # XXX ? pitch vel duration
            event.note(0, pitch, self.volume, duration)
            sequencer.send(event, ticks + begin)

    def to_midi(self, f, channel):
        """
        Create a MIDI expression for this melody.
        """

        scheduled = self.schedule_notes()

        track = 0

        for pitch, begin, duration in scheduled:
            begin = begin / self.tpb
            duration = duration / self.tpb
            f.addNote(track, channel, pitch, begin, duration, self.volume)

def melody_from_ly(s):
    """
    Make a `Melody` from a ly string.
    """

    g = LyeGrammar(s)
    ast = g.ast()
    ast = simplify_ast(ast)
    melody = Melody(ast, 120)
    return melody
