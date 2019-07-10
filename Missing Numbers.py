
# Given two array, one is main array and other is permutation of main array. Find the missing element in permutation
# array

from collections import Counter

len1 = int(input())
arr1 = list(map(int,input().split()))
len2 = int(input())
arr2 = list(map(int,input().split()))

elements = sorted(set(arr2))

count1 = Counter(arr1)
count2 = Counter(arr2)

missing = []

for i in elements:
    if count2[i]-count1[i]>0:
        missing.append(i)

print(*missing)

