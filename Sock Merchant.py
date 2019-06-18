
# From the given array find the number of pairs of the given item in list.

n = int(input())
ar = list(map(int, input().rstrip().split()))

nr = sorted(list(set(ar)))

count = []
for i in nr:
    count.append(ar.count(i))

pair = 0
for j in count:
    if j >= 2:
        pair+= j//2

print(pair)