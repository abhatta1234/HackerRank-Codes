
#Birthday Chocolate Problem!


total = int(input())
given = (list(map(int,input().split())))
parm = list(map(int,input().split()))

a=[]
for i in range(len(given)-parm[1]+1):
    b= []
    s= 0
    for j in range(parm[1]):
        b.append(given[i+s])
        s+=1
    if sum(b) == parm[0]:
        a.append(b)

print(len(a))


