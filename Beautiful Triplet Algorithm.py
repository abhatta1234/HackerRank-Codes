
#Beautiful Triplet using syntax. From a given array find the number of triplet(i,j,k) where i<j<k and j - i = k-j = d
#where d is the number given

from itertools import combinations

inp1 = input().split()
arr = list(map(int,input().split()))
d = int(inp1[1])
count = 0
for i in arr:
    if (i+d in arr) and (i+2*d in arr):
        count+=1

print(count)