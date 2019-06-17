
# From the array of the given list, find the most repeating one
# If there are two or more most repeating find the smallest one from them

from collections import Counter

num = int(input())

list = sorted(list(map(int,input().split())))

a = (Counter(list))

print(a)