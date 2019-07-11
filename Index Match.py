#Given two array print a list of (i,j) if A[i] = B[j]

num = int(input()) # Number of elements in arr1 and arr2
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

a = []
for i in range(num):
    ele = arr1[i]
    if ele in arr1 and ele in arr2:
        d = [i for i, val in enumerate(arr1) if val == ele]
        e = [i for i, val in enumerate(arr2) if val == ele]
        for i in d:
            for j in e:
                a.append((i,j))
print(a)

