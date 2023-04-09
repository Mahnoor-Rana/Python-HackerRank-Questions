#Find the Runner-Up Score!
if __name__ == '__main__':
    #n = int(input())
    arr ,n = map(int, input().split())
    arr = sorted(arr,reverse= True)
    i=0
    for i in arr:
        if (i < arr[0]):
             print(i)
             break