
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

if s == t:
    print("Yes")
elif sorted(set(a)) ==  sorted(set(b)):
    print("Yes")
elif len(s) + len(t) < k :
    print("Yes")
elif (len(s)+len(t)) - 2*count == k:
    print("Yes")
else:
    print("No")
