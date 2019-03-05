# coding=utf8
import re

acronyms = {
}

def searcher(f, use_parens=False):

    if use_parens == True:
        regex = something_cool
    else:
        regex = ur'[A-Z\.]{2,}'

    for line in f.splitlines():
        for m in re.finditer(regex, line):
            acronyms[m.group(0)] = m.group(0)
    return sorted(acronyms.keys())

