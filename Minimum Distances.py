
#Distance between two array values are defined as the number of indices between two values. Given a array, find the min
# imum distance between any pait of equal elements in the array. If no such value, print -1

num = int(input())

arr = list(map(int,input().split()))

nonre = set(arr)
comp = 10000
for i in nonre:
    if arr.count(i)%2==0:
        a = [ k for k, n in enumerate(arr) if n ==i]
        for j in range(arr.count(i)//2):
            comp = min(comp,a[j+1]-a[j])

if comp!= 10000:
    print(comp)
else:
    print(-1)


