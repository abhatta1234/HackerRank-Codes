# Given an array of integers, find and print the maximum number of integers you can select from the array such that the
# absolute difference between any two of the chosen integers is less than or equal to 1.

num = int(input())
arr = list(map(int,input().split()))
nonrep = sorted(list(set(arr)))
count = 0

if len(nonrep) == 1:
    count = arr.count(nonrep[0])
else:
    for i in range(len(nonrep)-1):
        count = max(count, arr.count(nonrep[i]))
        if nonrep[i] + 1  == nonrep[i+1]:
            count = max(count, arr.count(nonrep[i])+arr.count(nonrep[i+1]))

print(count)

