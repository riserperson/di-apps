# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

def searcher(f, use_parens):
    if use_parens == True:
        regex = ur"((?:[A-Z][a-z]+\s){2,})\(([A-Z]{2,})"
    else:
        regex = ur"([A-Z]{2,})"

    acronyms = {

    }
    for line in f:
        for m in re.finditer(regex, line):
            acronyms[m.group(0)] = m.group(0)
    return acronyms     
