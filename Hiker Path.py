
# Print the path of a hiker if up is given U is represented by "/" and down is given D and is represented by"\"
num = int(input())
word = input()
count= 0
arr=[]

for i in word:
    if i == "U":
        count+=1
        arr.append(count)
    else:
        count-=1
        arr.append(count)
row = max(arr)-min(arr)
print(count)
finarr = [[" "for y in range(num+2)] for x in range(row) ]

finarr[0][0] = "_"
finarr[0][num+1] = "_"
lev = 0
for i in range(1,num+1):
    if word[i-1] == "U":
        lev += 1
        print(lev)
        finarr[max(arr)-lev][i]="/"
    else:
        lev -= 1
        print(lev)
        finarr[abs(lev)][i]= "\\"

for i in finarr:
    print(*i,sep="")