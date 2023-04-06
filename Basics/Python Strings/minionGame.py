# Write a program to play a minion game

def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'or 'aeiou'# we can also do this
    s_score = 0
    k_score = 0
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            k_score+= n-i
        else :
            s_score+=n-i
    if s_score > k_score:
        print('Stuart', s_score)
    elif k_score > s_score:
         print('Kelvin', k_score)
    else:
        print('Draw')        

if __name__ == '__main__':
    s = input()
    minion_game(s)z