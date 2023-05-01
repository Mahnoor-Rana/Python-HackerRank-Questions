# Write a function
def is_leap(year):
    leap = False
    if year % 400 != 0 and year % 100 == 0: # for leap year
        leap = False
    elif year % 4 == 0:
        leap = True    
    
    return leap

year = int(input())
print(is_leap(year))