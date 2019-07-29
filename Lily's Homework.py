
num = int(input())
arr = list(map(int,input().split()))

def calc(a,b):
    m = {}
    for i in range(len(a)):
        m[a[i]]= i
    count = 0

    for i in range(len(b)):
        if a[i] != b[i]: # Checking if the item is in right index
            count+=1

            item1 = a[i] #assigning the item compared to a variable to avoid confusion after swapping
            item2 = b[i]

            i_swap = m[a[i]] # finding the index to swap
            f_swap = m[b[i]]

            a[i_swap],a[f_swap] = a[f_swap],a[i_swap] # swapping the items

            m[item1] = f_swap # updating the index after swapping
            m[item2] = i_swap
    return count


incr = calc(arr.copy(),sorted(arr)) # copy function is used to use the array. Without the copy function the arr indexing
# spits out weird results.
decr = calc(arr.copy(),sorted(arr,reverse = True))

print(min(incr,decr))




