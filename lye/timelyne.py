from __future__ import division

from fractions import gcd
from StringIO import StringIO

from lye.MidiFile import MIDIFile
from lye.instruments import (instruments as midi_instruments,
                             numbered_instruments)

INSTRUMENT, LYNE = range(2)

TACET = object()

def multipliers(numbers):
    denominator = reduce(gcd, numbers)
    numerator = max(numbers) // denominator
    lcm = denominator * numerator
    return [lcm // number for number in numbers]

def find_instrument(name):
    """
    Attempt to fully qualify a MIDI instrument name.
    """

    name = name.lower()
    found = []

    for instrument in midi_instruments:
        if instrument.startswith(name):
            found.append(instrument)

    if len(found) < 1:
        raise Exception("Couldn't match any instruments for %s" % name)
    elif len(found) > 1:
        raise Exception("Found multiple instruments for %s: %s"
            % (name, found))
    return found[0]

class Timelyne(object):
    """
    A song assembled from Lye snippets.
    """

    tempo = 120
    ticks_per_beat = 120

    _drum_channel = None
    _previous_lynes = None

    def __init__(self, library):
        self.channels = [[] for chaff in range(16)]
        self.library = library

    @classmethod
    def from_lines(cls, library, lines):
        """
        Parse a song from a series of lines.
        """

        self = cls(library)
        for line in lines:
            print "==="
            line = line.strip()
            marker, line = line[0], line[1:]
            if marker == "\\":
                # Directive. Add it and break.
                self.directive(line)
                continue

            tokens = [i.strip() for i in line.split("|")]
            if marker == ">":
                self.set_instruments(tokens)
            elif marker == "&":
                self.add_lynes(tokens)
            else:
                print "Unknown marker %s with line %r" % (marker, line)

        return self

    def directive(self, d):
        k, v = d.split("=")
        k = k.strip()
        v = int(v.strip())
        print "Directive: %s = %d" % (k, v)
        setattr(self, k, v)

    def set_instruments(self, instruments):
        for i, instrument in enumerate(instruments):
            if instrument == "drums":
                self._drum_channel = i
                print "%d: Drums"
                continue

            instrument = find_instrument(instrument)
            print "%d: Instrument %s" % (i, instrument)
            self.channels[i].append((INSTRUMENT, instrument))

    def add_lynes(self, names):
        melodies = []
        for i, name in enumerate(names):
            if name == '"':
                if self._previous_lynes:
                    melodies.append(self._previous_lynes[i])
                else:
                    raise Exception("Can't use \" in first lyne!")
            elif name == "-":
                melodies.append(TACET)
            else:
                snippet = self.library.snippets()[name]
                melodies.append(snippet.melody())

        self._previous_lynes = melodies

        lengths = []
        for m in melodies:
            if m is TACET:
                lengths.append(1)
            else:
                lengths.append(len(m))

        muls = multipliers(lengths)
        total = lengths[0] * muls[0]

        for i, melody in enumerate(melodies):
            if melody is TACET:
                print "%d: Tacet (%d)" % (i, total)
                self.channels[i].append((TACET, total))
            else:
                new = melody * muls[i]
                print "%d: Original %d, adjusted %d" % (i, len(melody),
                    len(new))
                self.channels[i].append((LYNE, new))

    def to_midi(self):
        f = MIDIFile(len(self.channels), ticksPerBeat=self.ticks_per_beat)

        time = [0] * len(self.channels)
        track = 0

        f.addTrackName(track, 0, "Lye")
        f.addTempo(track, 0, self.tempo)

        for channel, l in enumerate(self.channels):
            if self._drum_channel == channel:
                channel = 9
            for t, data in l:
                if t is INSTRUMENT:
                    f.addProgramChange(track, channel, time[channel],
                            numbered_instruments[data])
                elif t is LYNE:
                    for pitch, begin, duration in data.scheduled:
                        begin = begin / data.tpb + time[channel]
                        duration = duration / data.tpb
                        f.addNote(track, channel, pitch, begin, duration,
                                data.volume)
                    time[channel] += len(data) / self.ticks_per_beat
                elif t is TACET:
                    time[channel] += data / self.ticks_per_beat

        sio = StringIO()
        f.writeFile(sio)
        return sio.getvalue()
