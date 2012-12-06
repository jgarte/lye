#!/usr/bin/env python

import sys

from lye.combyne import Bynder, Combyned, Drumlyne
from lye.grammar import LyeGrammar
from lye.tiedye import play_a_bynder
from lye.utilities import find_instrument
from lye.visitors import simplify_ast

if len(sys.argv) < 3:
    print "Usage:", sys.argv[0], "(<instrument> <snippet>)+"
    sys.exit(0)

pairs = zip(sys.argv[1::2], sys.argv[2::2])

bound = Combyned()
for instrument, path in pairs:
    instrument = find_instrument(instrument)
    with open(path, "rb") as f:
        s = f.read()
        g = LyeGrammar(s)
        ast = g.lye()
        if instrument == "drums":
            bound |= Drumlyne(simplify_ast(ast))
        else:
            bound |= Bynder(simplify_ast(ast), instrument)

print "Playing..."

bound.tempo = 120
bound.ticks_per_beat = 120

ml = play_a_bynder(bound, "gugs.sf2")

from twisted.internet import reactor
reactor.callWhenRunning(ml.start, reactor)
reactor.run()
