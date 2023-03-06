
# You are given  lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

# CSS Code Pattern

# Selector
# {
# 	Property: Value;
# }

import re
expression = ".#[0-9A-Fa-f]{3,6}"

for i in range(int(input())):
    inpt = re.findall(expression, input())
    
    if inpt:
        for j in inpt:
            print(j[1:])