
# Sort the given array using pure algorithm, no in built function:

num = int(input())

arr = list(map(int,input().split()))

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        check = arr[i+1]
        while check <= arr[i] and i>=0 :
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = check
        print(*arr)
