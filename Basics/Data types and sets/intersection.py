# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(input().split())
m = str(input())
s = s.intersection(input().split())
print(len(s))