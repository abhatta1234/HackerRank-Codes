
# Perform the circular array rotation such that each element moves one unit to the unit with each rotation.
# And, print the elements at the index as per the query


constr = list(map(int,input().split()))
arr = list(map(int,input().split()))

rotct = constr[1]
leng = len(arr)
newarr = [0]*leng


for i in range(leng):
    indx = (i +rotct)%len(arr)
    newarr[indx] = arr[i]

rep = constr[2]

for i in range(rep):
    n = int(input())
    print(newarr[n])





