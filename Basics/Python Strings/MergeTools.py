

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    i =0
    while i < n:
        sub_s = string[i:i+k]
        uni_char = set(sub_s)
        uni_char = []
        for char in sub_s:
            if char not in uni_char:
                uni_char.append(char)
         
        print(''.join(uni_char))
        i+=k
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)