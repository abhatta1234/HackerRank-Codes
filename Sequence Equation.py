
# Given a sequence of an integer, find integer such that p(p(y)) = x

p = list(map(int,input().split()))

a = []
for i in range(1,len(p)+1):
    a.append(p.index(p.index(i)+1)+1)

print(*a,sep ="\n")



