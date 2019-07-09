#Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose
# index range covers the entire range of values in your array to sort. Each time a value occurs in the original array,
# you increment the counter at that index. At the end, run through your counting array, printing the value of each
# non-zero valued index that number of times.

num = int(input())

arr = list(map(int,input().split()))

zer = [0]*(max(arr)+1)

for i in arr:
    zer[i]+=1

print(*zer)