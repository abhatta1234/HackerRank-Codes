
#jumping on the cloud problem

num = int(input())

arr= list(map(int,input().split()))


a =[]
i = 0
while i < num-2:
    if arr[i+1] != 1 and arr[i+2] != 1:
            a.append(i+2)
            i+=2
    elif arr[i+1] ==1:
        a.append(i+2)
        i+=2
    else:
        a.append(i+1)
        i+=1

if i == num-2:
    print(len(a)+1)
else:
    print(len(a))



