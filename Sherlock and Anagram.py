
# Given a number of strings, find the number of pairs of substrings of the string that are anagrams of one another.

from collections import Counter

for i in range(int(input())):
    string = input()
    arr =[]
    for i in range(len(string)):
        for j in range(i,len(string)):
            arr.append("".join(sorted(string[i:j+1])))
    a = Counter(arr)
    val = 0
    ecount = 0

    for i in a:
        if a[i] > 1:
            val+=(a[i])*(a[i]-1)*.5
    print(int(val))
