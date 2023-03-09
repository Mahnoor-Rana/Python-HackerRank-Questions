#write a program to find angle MBC
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import atan, degrees
AB = int(input())
BC = int(input())

angleC = atan(AB/BC)
deg = degrees(angleC)
print((round(deg)),chr(176),sep='') 