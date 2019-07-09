# Given a binary string, count the number of alterations required such that it doesn't contain substring "010". In one
#step 0 can be changed to 1 and vice-versa.

num = int(input())
a = input()
i = 0
count = 0
while i < len(a)-2:
    if a[i] == "0" and a[i+1] == "1" and a[i+2] == "0":
        count+=1
        i+=3
    else:
        i+=1
print(count)
