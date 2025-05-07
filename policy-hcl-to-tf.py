#!/usr/bin/env python3

# Only Knuth can judge me

import fileinput

def process_rule(text):
    elements = text.split("\n")
    path = elements[1].split(" ")[1]
    description = elements[0][2:]
    out = "  rule {\n"
    out += f"    path         = {path}\n"
    out += f"  {elements[2]}\n"
    out += f"    description  = \"{description}\"\n"
    out += "  }\n"
    print(out)

collected = ""
for line in fileinput.input():
    if line.startswith("###"):
        print(line)
    elif line == "\n":
        process_rule(collected)
        collected = ""
    else:
        collected += line

