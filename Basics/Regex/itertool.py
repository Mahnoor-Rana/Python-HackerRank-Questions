# Write a program to print cartesian product
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
import itertools
A = sorted(map(int,input().split()))
B = sorted(map(int,input().split()))
for product in itertools.product(A,B):
    print(product, end=" ")
