# Neo has a complex matrix script. The matrix script is a  X  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

# Capture.JPG

# To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.

# If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.

# Neo feels that there is no need to use 'if' conditions for decoding.

# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].


#!/bin/python3
import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

transponded = "".join([matrix[j][i] for i in range(m) for j in range(n)])

ending = re.search("[^a-zA-Z0-9]*$", transponded).group()[1:]
middle = re.sub("[^a-zA-Z0-9]+", " ", transponded).strip()
begining = re.search("^[^a-zA-Z0-9]*", transponded).group()[:-1]

result = ""
result += begining
result += middle
result += ending

print(result)