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
        input_str = line
        matches = re.finditer(regex, input_str, re.MULTILINE)
        for matchNum, match in enumerate(matches, start=1):
            if match.group(1) not in acronyms.keys():
                if use_parens == True:
                    acronyms[match.group(1)] = match.group(2)
                else:
                    acronyms[match.group(1)] = match.group(1)
                return acronyms
