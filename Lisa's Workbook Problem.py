
# a workbook contains exercise problems grouped into chapters. A problem is special if its index(with in the chapter)
# is same as the page number. One page can only have max k number of problems.

inp1 = list(map(int,input().split()))
k = inp1[1]
a = list(map(int,input().split()))
outarr=[]
add = [i+1 for i in range(k)]
for i in a:
    inarr = []
    (div,rem)=(i//k,i%k if i%k!=0 else 0)
    if div!=0:
        for j in range(div):
            mult = [k*j for i in range(k)]
            inarr =[mult[i]+add[i] for i in range(k)]
            outarr.append(inarr)
        if rem!=0:
            outarr.append([k*(j+1)+(i+1) for i in range(rem)])

        else:
        c = [i+1 for i in range(rem)]
        outarr.append(c)
count = 0
for i in range(len(outarr)):
    if i+1 in outarr[i]:
        count+=1
print(count)
print(outarr) #This prints the page distribution.