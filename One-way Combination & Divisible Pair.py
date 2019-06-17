

num = (list(map(int,input().split())))

ar = list(map(int,input().split()))
count = 0
a =[]
for i in range(num[0]):
    for j in range(i,num[0]):
        if i != j:
            sum = ar[i]+ar[j]
            a.append([ar[i],ar[j]])
            if i < j and sum%num[1]==0:
                count+=1
print(count)
