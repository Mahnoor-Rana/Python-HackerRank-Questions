#Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

import re

for _ in range(int(input())):
    s = input()
    if re.search(r'<[a-zA-Z][\w\-.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', s):
        print(s)
