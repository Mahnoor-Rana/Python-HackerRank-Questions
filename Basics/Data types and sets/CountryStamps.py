# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of  country stamps.
#Find the total number of distinct country stamps.

n = int(input())
unique_name= set()
for i in range(n):
    names = input().strip()
    unique_name.add(names)
count = len(unique_name)
print(count)