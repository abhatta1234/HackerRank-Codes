arr = list(map(int,input().split())) # Taking inputs
inp = list(input())

count = 0 # initiating variable for count
n_count = 0
const = arr[1]

indx = {i:inp[i] for i in range(len(inp))} # Hash map to expedite the indexing process
ls_indx = []

for i in range(len(inp)//2):
    mval = max(int(indx[i]), int(indx[len(inp) - i - 1]))
    if inp[i] != inp[len(inp) - i - 1]:
        count+=1
        if int(indx[i]) > int(indx[len(inp)-i-1]):
            indx[len(inp) - i - 1] = mval
        else:
            indx[i] = mval
    if mval == 9:
         if not (int(indx[i]) == 9 and int(indx[len(inp) - i - 1]) == 9):
            n_count+=1
palin = [int(v) for v in indx.values()]

rem = const - n_count
ind = 0

while rem > 1 and ind <= len(palin)-1:
    if palin[ind] != 9:
        palin[ind] = 9
        palin[len(palin)-ind-1]= 9
        rem-=2
    ind+=1

if len(palin)%2!= 0 and rem == 1:
    palin[len(palin)//2]=9


if const>=count:
    print("".join(map(str,palin)))
else:
    print(-1)



