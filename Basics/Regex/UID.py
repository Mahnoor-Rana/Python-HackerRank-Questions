# ABCXYZ company has up to 100 employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.

import re
# Read number of test cases
t = int(input().strip())

# Loop through test cases
for _ in range(t):
    uid = input().strip()
    
    # Check length
    if len(uid) != 10:
        print("Invalid")
        continue
    
    # Check for alphanumeric characters only
    if not uid.isalnum():
        print("Invalid")
        continue
    
    # Check for at least 2 uppercase characters
    if len(re.findall(r'[A-Z]', uid)) < 2:
        print("Invalid")
        continue
    
    # Check for at least 3 digits
    if len(re.findall(r'\d', uid)) < 3:
        print("Invalid")
        continue
    
    # Check for repeating characters
    if len(set(uid)) != 10:
        print("Invalid")
        continue
    
    # All checks passed, UID is valid
    print("Valid")