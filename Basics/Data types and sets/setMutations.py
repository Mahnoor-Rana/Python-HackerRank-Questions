# You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

# Your task is to execute those operations and print the sum of elements from set .

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
