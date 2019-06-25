
# ACM ICPC Team Problem

from itertools import combinations
num = list(map(int,input().split()))

a = [input() for i in range(num[0])]

index = [i for i in range(num[0])]

b = list(combinations(index,2))

col = []

for i in b:
    c = bin(int(a[i[0]],2)|int(a[i[1]],2))[2:]

    d = sum(list(map(int,c)))

    col.append(d)

print(max(col))

print(col.count(max(col)))

