# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m= int(input())
s = set(input().split())
m = int(input())
s = s.symmetric_difference(input().split())
print(len(s))