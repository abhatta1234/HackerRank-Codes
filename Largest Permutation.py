# You are given an unordered array of unique integers incrementing from . You can swap any two elements a limited
# number of times. Determine the largest lexicographical value array that can be created by executing no more than the
# limited number of swaps

# Hash map is created so that index can be found in O(1) time.

given = list(map(int,input().split()))
arr = list(map(int,input().split()))
hashmap = {a:b for b,a in enumerate(arr)}
rev = sorted(arr)[::-1]
i = 0
check = 0
if given[1]>given[0]:
    arr = rev
else:
    while check < given[1] and i < len(arr): #check is the counter for swap. You might not need to swap to put in order.
        ind = hashmap[rev[i]]
        if i!= ind:
            hashmap[rev[i]], hashmap[arr[i]] = hashmap[arr[i]], hashmap[rev[i]]
            arr[ind] = arr[i]
            arr[i] = rev[i]
            check+=1
        i+=1
print(*arr)

# This code is same as above but since it traverses along the list to find index. It takes longer time.

# given = list(map(int,input().split()))
# arr = list(map(int,input().split()))
# rev = sorted(arr)[::-1]
# i = 0
# check = 0
# if given[1]>given[0]:
#     arr = rev
# else:
#     while check < given[1] and i < len(arr): #check is the counter for swap. You might not need to swap to put in order.
#         ind = arr.index(rev[i])
#         if i!= ind:
#             arr[ind] = arr[i]
#             arr[i] = rev[i]
#             check+=1
#         i+=1
# print(*arr)

