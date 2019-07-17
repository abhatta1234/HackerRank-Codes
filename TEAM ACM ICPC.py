from itertools import combinations
from collections import Counter

num = list(map(int, input().split()))
a = [input() for i in range(num[0])]
b = list(combinations(a, 2))

col = []
check = 0

for i in b:
    c = (bin(int(i[0], 2) | int(i[1], 2))[2:])
    d = Counter(c)
    if d['1']>check:
        check = d['1']
        count = 1
    elif d['1'] == check:
        count+=1
print(check)
print(count)

