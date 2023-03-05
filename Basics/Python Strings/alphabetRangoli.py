# Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

import string
def print_rangoli(size):
    # your code goes here
    l = string.ascii_lowercase[:size]
    w = 4*size-3
    
    for i in range(size-1,0,-1):
         line = '-'.join(l[size-1:i:-1] + l[i:size])
         print(line.center(w,'-'))
         
    for i in range(size):
        line = '-'.join(l[size-1:i:-1]+l[i:size])
        print(line.center(w,'-'))
         
         
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)