# Perform different functions 
n = int(input())
s = set(map(int, input().split()))
c = []
for _ in range(int(input())):
    op = input().split()
    
    if op[0] == "remove":
        s.remove(int(op[1]))
    if op[0] == "discard":
        s.discard(int(op[1]))
    if op[0] == "pop":
        s.pop()
print(sum( s))  