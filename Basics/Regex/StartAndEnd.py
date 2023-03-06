# You are given a string s.
# Your task is to find the indices of the start and end of string k in S.


import re
s,k = input(),input()
patter = re.compile(k)
m=patter.search(s)

if not m:
        print((-1,-1))  
while m:
    print((m.start(),m.end()-1))
    m=patter.search(s,m.start()+1)