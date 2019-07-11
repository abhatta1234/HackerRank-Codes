
# Given two array and a number. Check if the permutation of array can make sum of both array element at same index more
# than or equal to the given number


for i in range(int(input())):
    given = list(map(int,input().split()))
    const = given[1]

    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))

    arr1.sort()
    arr2.sort(reverse = True)

    ans = "NO"
    if(all(arr1[i]+arr2[i] >= const for i in range(len(arr1)))):
            ans = "YES"
    print(ans)