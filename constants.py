HEAD_SLICE = slice(0, 7)
SECTION_SLICE = slice(0, 2)
SUB_SECTION_SLICE = slice(2, 4)
SUB_SUB_SECTION_SLICE = slice(4, 7)
PREDICATE_SLICE = slice(7, None)


BAD_SUFFIXES = [
    ".bad",
    ".er",
    ".err",
    ".error",
]