# Sort the given array by counting not by comparison.

# Counting the repitition:
num = int(input())
arr = list(map(int,input().split()))
zer = [0]*(max(arr)+1)
for i in arr:
    zer[i]+=1
#Sorting the array on the basis of count
sortd = []
val = 0
for i in zer:
    for j in range(i):
        sortd.append(val)
    val+=1

print(*sortd)
