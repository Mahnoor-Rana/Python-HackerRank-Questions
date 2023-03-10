#write a program to find angle MBC
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan, degrees
AB = int(input())
BC = int(input())

angleC = atan(AB/BC)
print((round(degrees(angleC))),chr(176),sep='') 