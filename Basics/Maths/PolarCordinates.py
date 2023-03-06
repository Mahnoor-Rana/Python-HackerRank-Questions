#You are given a complex  Z . Your task is to convert it to polar coordinates.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath as cm
import math
z=complex(input())
print(abs(z))
ph = cm.phase(z)
print(ph)


