
# Electronics Shop Problem

# From a set of two array find the max sum of element from array. Constraint number is given.

inp = list(map(int,input().split()))
keyboards = list(map(int,input().split()))
drives = list(map(int,input().split()))
a=[]
for i in keyboards:
    for j in drives:
        if (i+j)<=b:
            a.append(i+j)
if a:
    return(max(a))
else:
    return(-1)

