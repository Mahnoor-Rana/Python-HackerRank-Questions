# Find whether set A is a subset of set B.
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    a_len = int(input())
    a = set(map(int,input().split()))
    b_len = int(input())
    b = set(map(int,input().split()))
    print(a.issubset(b))

