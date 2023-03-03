# Given 2 sets of integers,  and m , n print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either m or n  but do not exist in both.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

c = sorted(a.symmetric_difference(b))
for i in c:
    print(i)
