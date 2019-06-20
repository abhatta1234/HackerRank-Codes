
# Jumping on the cloud revisited problem


const = list(map(int,input().split()))
arr = list(map(int,input().split()))
rotarr = [i for i in range(const[0])]

e = 100

indx = const[1]%const[0]

while rotarr[indx] != 0 :
    if arr[indx] == 0:
        e = e -1
    else:
        e = e - 3
    print((indx,e))
    indx = (indx + const[1])%const[0]


if arr[0] == 0:
    e = e - 1
else:
    e = e- 3

print(e)


