
#Given a set of distinct integers, print the size of maximal subset of S where the sum of any 2 numbers in S is not
# Evenly divisible by k

const = list(map(int,input().split()))
arr = list(map(int,input().split()))
remarr = [i%const[1] for i in arr]
sortd = sorted(list(set(remarr)))

div = const[1]
count = 0

if div%2 !=0 :
    if remarr.count(0)!= 0:
        count = 1
    for i in range(1,div//2+1):
        count+= max(remarr.count(i),remarr.count(const[1]-i))
else:
    if remarr.count(0)!=0:
        count = 1
    if remarr.count(div/2) !=0:
        count+=1
    for i in range(1,div//2):
        count+= max(remarr.count(i),remarr.count(const[1]-i))
print(count)


