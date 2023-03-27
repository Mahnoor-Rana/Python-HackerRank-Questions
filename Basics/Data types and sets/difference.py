# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
m = int(input())
s = set(input().split())
s = s.difference(input().split())
print(len(s))