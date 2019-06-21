
# Append and delete challenge. check whether the given string s can be converted to string t by exactly performing
# k number of operations. The operation can be either appending one digit or deleting one.

s = input()
t = input()
k = int(input())

a = min(len(s),len(t))

count = 0

for x,y in zip(s,t):
    if x == y:
        count +=1
    else:
        break
if (len(s)+len(t) - 2*count) == k:
    print("Yes")
elif len(s)+len(t) < k:
    print("Yes")
elif k>(len(s)+len(t)-2*count) and k%2 == (len(s)+len(t)-2*count)%2:
    print("Yes")
else:
    print("No")
