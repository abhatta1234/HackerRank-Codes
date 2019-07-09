#Given a list of unsorted integers,arr,find the pair of elements that have the smallest absolute difference between
# them. If there are multiple pairs, find them all.

import sys

num = int(input())
arr = sorted(list(map(int,input().split())))

min = sys.maxsize
a = []

for i in range(len(arr)-1):
    if abs(arr[i]-arr[i+1]) < min:
        min = abs(arr[i]-arr[i+1])
        a = []
        b = [arr[i],arr[i+1]]
        a.extend(b)
    elif abs(arr[i]-arr[i+1]) == min:
        b = [arr[i], arr[i + 1]]
        a.extend(b)

print(*a)