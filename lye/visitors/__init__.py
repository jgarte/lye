from lye.visitors.maps import (ChordSorter, DrumsTransformer, DurationVisitor,
                               DynamicRemover, Legato, MusicFlattener,
                               NoteTransformer, Relativizer, TimesVisitor,
                               VoicesTransformer)
from lye.visitors.peephole import RestMerger, TieRemover
from lye.visitors.pegs import SlurMaker

simplify_stages = (
    # Get our ASTs into the shape we want. Mostly, do our folds and eliminate
    # certain nodes.
    # Drums -> ().
    DrumsTransformer,
    # Music -> Voice inside Voice.
    VoicesTransformer,
    # Fold durations.
    DurationVisitor,
    # Times -> Music. Must come after durations.
    TimesVisitor,
    # Relative -> Music.
    Relativizer,
    # Remove any spare Musics. Must be done before peepholes.
    MusicFlattener,
    # Note -> SciNote.
    NoteTransformer,
    # Fold Dynamics. Must come after SciNotes.
    DynamicRemover,
    # Sort Chord contents. Must come after SciNotes.
    ChordSorter,
    # Remove TIEs.
    TieRemover,
    # Add Slurs.
    SlurMaker,
    # Merge Rests.
    RestMerger,
)


express_stages = (
    # Main exprssion generator.
    Legato,
    # Remove extra Musics generated by Legato.
    MusicFlattener,
    # Merge Rests generated by Legato.
    RestMerger,
)


def simplify_ast(ast):
    for stage in simplify_stages:
        ast = stage().visit(ast)
    return ast

def express_ast(ast, instrument):
    for stage in express_stages:
        ast = stage(instrument).visit(ast)
    return ast
