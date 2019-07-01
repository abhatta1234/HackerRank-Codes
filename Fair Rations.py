
# Given an array, if you add +1 to any item you must also add +1 to item before and after it. Find the number performing
#such action to convert the list to an even array. If not, print("NOT").

num = int(input())
arr = list(map(int,input().split()))
count = 0

if sum(arr)%2 == 0:
    for i in range(len(arr)-1):
        if arr[i]%2 != 0:
            count+=2
            arr[i] =arr[i]+1
            arr[i+1]=arr[i+1]+1
    print(count)
else:
    print('NO')

