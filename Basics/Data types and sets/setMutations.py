# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

# Your task is to execute those operations and print the sum of elements from set A .

n = (input())
a = set(map(int,input().split()))

for _ in range(int(input())):
    op,n =input().split()
    b = set(map(int,input().split()))
    
    if op == "intersection_update":
        a.intersection_update(b)
    elif op == "difference_update":
        a.difference_update(b)
    elif op == "symmetric_difference_update":
        a.symmetric_difference_update(b)
    elif op == "update":
        a.update(b)
print(sum(a))
