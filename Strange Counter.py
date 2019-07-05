num = int(input())
rep = 3
count = 0
a = 0
while num> count:
    a+=1
    lastrec = count + 1
    count+= rep
    rep = rep*2
start = 3*2**(a-1)
distance = num - lastrec
print(start - distance)