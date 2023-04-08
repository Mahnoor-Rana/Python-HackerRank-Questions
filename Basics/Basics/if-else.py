import math
import os
import random
import re
import sys
if __name__ == '__main__':
    m = int(input().strip()) # split() also use this 
    if m%2!=0:
        print("Weird")
    elif m >=2 and m <= 5 or m > 20:
        print("Not Weird")
    else:
        print("Weird")