
# Given an array check whether the array can be sorted by either swapping two digits or reversing one of the substring.

num  = int(input())
arr = list(map(int,input().split()))
swap_arr = arr.copy()
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        val = i
        while val < len(arr) -1 and arr[i]>arr[val+1]:
            val+=1
        break
swap_arr[i],swap_arr[val] = swap_arr[val],swap_arr[i]
if swap_arr == sorted(arr):
    print('yes')
    print('swap', i + 1, val + 1)
elif arr[:i] + sorted(arr[i:val+1]) + arr[val + 1:] == sorted(arr):
    print('yes')
    print('reverse', i + 1, val + 1)
else:
    print('no')
