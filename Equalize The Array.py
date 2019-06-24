
#Given an array of integers. Find out the minimum numbers of steps to reduce the array until all remaining are equal.

from collections import Counter

num = int(input())

arr = list(map(int,input().split()))

mostrep = max(list(Counter(arr).values()))

print(len(arr) - mostrep)