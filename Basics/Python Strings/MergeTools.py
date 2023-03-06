# There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A' characters, so . The second substring has all distinct characters, so . The third substring has  different characters, so . Note that a subsequence maintains the original order of characters encountered. The order of characters in each subsequence shown is important.

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