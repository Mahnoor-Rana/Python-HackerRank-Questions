# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = int(input())
s = set(input().split())
s = s.intersection(s)
print(len(s))