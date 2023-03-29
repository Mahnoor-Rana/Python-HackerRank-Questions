#Complete the swap_case function 
# swap_case has the following parameters:
# string s: the string to modify

def swap_case(s):
    s_1="abc"
    for char in s:
        if char.islower():
            s_1 += char.upper()
            
        elif char.isupper():
            s_1 += char.lower()
            
        else:
            s_1 += char 
    return s_1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)