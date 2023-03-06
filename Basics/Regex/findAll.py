# Task
# You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of S that contains 2  or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only.


# its kind of look tough but its easy
# (?<=x)y will return y if there is xy in order
# y(?=x) will return x if xy in order
# {2,} is used to only match those which occur 2 or more than 2 times
# (?<=x)y(?=x) overall regex is to find more than occurence of y between distinct char


import re
i = input()
match = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([aeiouAIEOU]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',i)
if match:
    print('\n'.join(match))
else:
    print(-1)