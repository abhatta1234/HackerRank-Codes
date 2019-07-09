
# Given a numeric string, find out if the string can be split into a sequence of string where without any arrangements
# and no leading zeros satisfies, a[i]-a[i-1]=1. Example; 99100 split into "99"&"1000". "1234" into "1","2","3" &"4".

num = int(input())
for _ in range(num):
    a = input()
    check = 0
    for i in range(len(a)//2):
        emp = ""
        start = a[:i+1]
        emp = start
        j=1
        while len(emp)<len(a):
            emp+= str(int(start)+j)
            j+=1
        if emp == a:
            print("YES",a[:i+1])
            check+=1
            break
    if check ==0 :
        print("NO")

