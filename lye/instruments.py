from lye.types import Note

instruments = [
    "acoustic grand",
    "bright acoustic",
    "electric grand",
    "honky-tonk",
    "electric piano 1",
    "electric piano 2",
    "harpsichord",
    "clav",
    "celesta",
    "glockenspiel",
    "music box",
    "vibraphone",
    "marimba",
    "xylophone",
    "tubular bells",
    "dulcimer",
    "drawbar organ",
    "percussive organ",
    "rock organ",
    "church organ",
    "reed organ",
    "accordion",
    "harmonica",
    "concertina",
    "acoustic guitar (nylon)",
    "acoustic guitar (steel)",
    "electric guitar (jazz)",
    "electric guitar (clean)",
    "electric guitar (muted)",
    "overdriven guitar",
    "distorted guitar",
    "guitar harmonics",
    "acoustic bass",
    "electric bass (finger)",
    "electric bass (pick)",
    "fretless bass",
    "slap bass 1",
    "slap bass 2",
    "synth bass 1",
    "synth bass 2",
    "violin",
    "viola",
    "cello",
    "contrabass",
    "tremolo strings",
    "pizzicato strings",
    "orchestral strings",
    "timpani",
    "string ensemble 1",
    "string ensemble 2",
    "synthstrings 1",
    "synthstrings 2",
    "choir aahs",
    "voice oohs",
    "synth voice",
    "orchestra hit",
    "trumpet",
    "trombone",
    "tuba",
    "muted trumpet",
    "french horn",
    "brass section",
    "synthbrass 1",
    "synthbrass 2",
    "soprano sax",
    "alto sax",
    "tenor sax",
    "baritone sax",
    "oboe",
    "english horn",
    "bassoon",
    "clarinet",
    "piccolo",
    "flute",
    "recorder",
    "pan flute",
    "blown bottle",
    "shakuhachi",
    "whistle",
    "ocarina",
    "lead 1 (square)",
    "lead 2 (sawtooth)",
    "lead 3 (calliope)",
    "lead 4 (chiff)",
    "lead 5 (charang)",
    "lead 6 (voice)",
    "lead 7 (fifths)",
    "lead 8 (bass+lead)",
    "pad 1 (new age)",
    "pad 2 (warm)",
    "pad 3 (polysynth)",
    "pad 4 (choir)",
    "pad 5 (bowed)",
    "pad 6 (metallic)",
    "pad 7 (halo)",
    "pad 8 (sweep)",
    "fx 1 (rain)",
    "fx 2 (soundtrack)",
    "fx 3 (crystal)",
    "fx 4 (atmosphere)",
    "fx 5 (brightness)",
    "fx 6 (goblins)",
    "fx 7 (echoes)",
    "fx 8 (sci-fi)",
    "sitar",
    "banjo",
    "shamisen",
    "koto",
    "kalimba",
    "bagpipe",
    "fiddle",
    "shanai",
    "tinkle bell",
    "agogo",
    "steel drums",
    "woodblock",
    "taiko drum",
    "melodic tom",
    "synth drum",
    "reverse cymbal",
    "guitar fret noise",
    "breath noise",
    "seashore",
    "bird tweet",
    "telephone ring",
    "helicopter",
    "applause",
    "gunshot",
]

numbered_instruments = dict((k, i) for i, k in enumerate(instruments))

bounds = {
    "acoustic grand": (0, 88),
    "bright acoustic": (0, 88),
    "electric grand": (0, 88),
    "honky-tonk": (0, 88),
    "electric piano 1": (0, 88),
    "electric piano 2": (0, 88),
    "harpsichord": (0, 88),
    "clav": (0, 88),
    "celesta": (0, 88),
    "glockenspiel": (0, 88),
    "music box": (0, 88),
    "vibraphone": (0, 88),
    "marimba": (0, 88),
    "xylophone": (0, 88),
    "tubular bells": (0, 88),
    "dulcimer": (0, 88),
    "drawbar organ": (0, 88),
    "percussive organ": (0, 88),
    "rock organ": (0, 88),
    "church organ": (0, 88),
    "reed organ": (0, 88),
    "accordion": (0, 88),
    "harmonica": (0, 88),
    "concertina": (0, 88),
    "acoustic guitar (nylon)": (40, 88), # E2 - E6
    "acoustic guitar (steel)": (40, 88),
    "electric guitar (jazz)": (40, 88),
    "electric guitar (clean)": (40, 88),
    "electric guitar (muted)": (40, 88),
    "overdriven guitar": (35, 88), # B1 - E6 (seven string)
    "distorted guitar": (35, 88),
    "guitar harmonics": (52, 88), # E3 is the lowest one possible
    "acoustic bass": (28, 67), # E1 - G4
    "electric bass (finger)": (23, 67), # B0 - G4 (five string)
    "electric bass (pick)": (23, 67),
    "fretless bass": (28, 67),
    "slap bass 1": (23, 67),
    "slap bass 2": (23, 67),
    "synth bass 1": (28, 67),
    "synth bass 2": (28, 67),
    "violin": (0, 88),
    "viola": (0, 88),
    "cello": (0, 88),
    "contrabass": (0, 88),
    "tremolo strings": (0, 88),
    "pizzicato strings": (0, 88),
    "orchestral strings": (0, 88),
    "timpani": (0, 88),
    "string ensemble 1": (0, 88),
    "string ensemble 2": (0, 88),
    "synthstrings 1": (0, 88),
    "synthstrings 2": (0, 88),
    "choir aahs": (0, 88),
    "voice oohs": (0, 88),
    "synth voice": (0, 88),
    "orchestra hit": (0, 88),
    "trumpet": (60, 84), # C4 - C6 (R-K)
    "trombone": (34, 70), # Bb1 - Bb4 (R-K)
    "tuba": (0, 88),
    "muted trumpet": (60, 84), # C4 - C6 (R-K)
    "french horn": (0, 88),
    "brass section": (0, 88),
    "synthbrass 1": (0, 88),
    "synthbrass 2": (0, 88),
    "soprano sax": (56, 87), # Ab3 - Eb6
    "alto sax": (49, 80), # Db3 - Ab5
    "tenor sax": (44, 75), # Ab2 - Eb5
    "baritone sax": (37, 68), # Db2 - Ab4
    "oboe": (0, 88),
    "english horn": (0, 88),
    "bassoon": (0, 88),
    "clarinet": (0, 88),
    "piccolo": (0, 88),
    "flute": (0, 88),
    "recorder": (0, 88),
    "pan flute": (0, 88),
    "blown bottle": (0, 88),
    "shakuhachi": (0, 88),
    "whistle": (0, 88),
    "ocarina": (0, 88),
    "lead 1 (square)": (0, 88),
    "lead 2 (sawtooth)": (0, 88),
    "lead 3 (calliope)": (0, 88),
    "lead 4 (chiff)": (0, 88),
    "lead 5 (charang)": (0, 88),
    "lead 6 (voice)": (0, 88),
    "lead 7 (fifths)": (0, 88),
    "lead 8 (bass+lead)": (0, 88),
    "pad 1 (new age)": (0, 88),
    "pad 2 (warm)": (0, 88),
    "pad 3 (polysynth)": (0, 88),
    "pad 4 (choir)": (0, 88),
    "pad 5 (bowed)": (0, 88),
    "pad 6 (metallic)": (0, 88),
    "pad 7 (halo)": (0, 88),
    "pad 8 (sweep)": (0, 88),
    "fx 1 (rain)": (0, 88),
    "fx 2 (soundtrack)": (0, 88),
    "fx 3 (crystal)": (0, 88),
    "fx 4 (atmosphere)": (0, 88),
    "fx 5 (brightness)": (0, 88),
    "fx 6 (goblins)": (0, 88),
    "fx 7 (echoes)": (0, 88),
    "fx 8 (sci-fi)": (0, 88),
    "sitar": (0, 88),
    "banjo": (0, 88),
    "shamisen": (0, 88),
    "koto": (0, 88),
    "kalimba": (0, 88),
    "bagpipe": (0, 88),
    "fiddle": (0, 88),
    "shanai": (0, 88),
    "tinkle bell": (0, 88),
    "agogo": (0, 88),
    "steel drums": (0, 88),
    "woodblock": (0, 88),
    "taiko drum": (0, 88),
    "melodic tom": (0, 88),
    "synth drum": (0, 88),
    "reverse cymbal": (0, 88),
    "guitar fret noise": (0, 88),
    "breath noise": (0, 88),
    "seashore": (0, 88),
    "bird tweet": (0, 88),
    "telephone ring": (0, 88),
    "helicopter": (0, 88),
    "applause": (0, 88),
    "gunshot": (0, 88),
}

NEAREST, LOWEST, HIGHEST = range(3)

def top_margin(melody, bound):
    i = max(note.pitch for note in melody.notes if isinstance(note, Note))
    return bound - i

def bottom_margin(melody, bound):
    i = min(note.pitch for note in melody.notes if isinstance(note, Note))
    return i - bound

def fit(melody, instrument, strategy=NEAREST):
    bottom_bound, top_bound = bounds[instrument]
    top = top_margin(melody, top_bound)
    bottom = bottom_margin(melody, bottom_bound)
    if top + bottom < 0:
        raise Exception("Couldn't ever fit this melody!")

    if strategy == NEAREST:
        strategy = HIGHEST if top < 0 else LOWEST

    if strategy == LOWEST:
        octaves = bottom // 12
        adjustment = octaves * 12
        notes = []
        for note in melody.notes:
            if isinstance(note, Note):
                note = note._replace(pitch=note.pitch - adjustment)
            notes.append(note)
        melody.notes = notes
    elif strategy == HIGHEST:
        octaves = top // 12
        adjustment = octaves * 12
        notes = []
        for note in melody.notes:
            if isinstance(note, Note):
                note = note._replace(pitch=note.pitch + adjustment)
            notes.append(note)
        melody.notes = notes