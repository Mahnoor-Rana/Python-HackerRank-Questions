# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(input().split())
m = int(input())
s = s.union(input().split())
print(len(s))