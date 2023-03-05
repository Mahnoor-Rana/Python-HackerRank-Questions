# Design the mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
for i in range(n):
    if i < n//2:
        print((".|."*(2*i+1)).center(m,"-"))
    elif i == n//2:
        print("WELCOME".center(m,"-"))
    else:
        print((".|."*(2*(n-i-1)+1)).center(m,"-"))
