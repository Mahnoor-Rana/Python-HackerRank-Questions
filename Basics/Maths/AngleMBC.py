#write a program to find angle MBC
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan, degrees
a = int(input())
b = int(input())

angleC = atan(a/b)
print((round(degrees(angleC))),chr(176),sep='') 