
# Given the array of the string of lower case ascii, fing the number of characters that appears in all the string.

num = int(input())
a = []
for i in range(num):
    a.append(set(input()))
common = a[0].intersection(a[1])
for j in range(len(a)-1):
    test = a[j].intersection(a[j+1])
    common = common.intersection(test)
print(len(common))