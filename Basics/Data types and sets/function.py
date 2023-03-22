
# write function
def print_full_name(first, last):
    # Write your code here
   # first = (input())
   # last = (input())
    print('Hello'+ " " + first+" "+ last + "! You just delved into python.")
if __name__ == '__main__':
    first_name = input().split()
    last_name = input().split()
    print_full_name(first_name, last_name)

def name(f,l):
    print('hey'+f,l)