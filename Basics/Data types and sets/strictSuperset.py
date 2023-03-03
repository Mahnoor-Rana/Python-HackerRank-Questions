# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int, input().split()))
n = int(input())
b = set(map(int,input().split()))
c =set(map(int,input().split()))
s = a.issuperset(c)
print(s)
    
 