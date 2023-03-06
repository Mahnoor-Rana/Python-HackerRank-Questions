# Enter your code here. Read input from STDIN. Print output to STDOUT
# The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
# The method is called for all matches and can be used to modify strings in different ways.
# The re.sub() method returns the modified string as an output.
#You are given a text of  lines. The text contains && and || symbols.
#Your task N is to modify those symbols to the following
import re
n = int(input())
def reSub(line):
    line = re.sub(r"(?<=\s)&&(?=\s)", "and", line)
    line = re.sub(r"(?<=\s)\|\|(?=\s)", "or", line)
    return line
for i in range(n):
    line =input()
    line = reSub(line)
    print(line)