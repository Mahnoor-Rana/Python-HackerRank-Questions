#   Write a program to captalize first char of word

import math
import os
import random
import re
import sys

import string

def solve(s):
    return string.capwords(s, sep=' ')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input() # str(input())

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
