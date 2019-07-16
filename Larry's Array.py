
# Solution of this problem is based on the 15 tiles problem. If the summation of the count of number less than itself
# in the right is even, then it is solvable. Else, it is not!
n = int(input())

for i in range(n):
    count = 0
    num = int(input())
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                count+=1
    print(count)
    if count %2 == 0:
        print("YES")
    else:
        print("NO")