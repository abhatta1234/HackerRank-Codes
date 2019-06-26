
#Beautiful Triplet using syntax. From a given array find the number of triplet(i,j,k) where i<j<k and j - i = k-j = d
#where d is the number given 

from itertools import combinations

inp1 = input().split()
arr = list(map(int,input().split()))
d = int(inp1[1])

a = [i for i in combinations(arr,3) if i[0]<i[1]<i[2] and i[1]-i[0] == d and i[2]-i[1] == d ]

print(len(a))