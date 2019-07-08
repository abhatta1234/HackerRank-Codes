

const = list(map(int,input().split()))
given = [list(map(int,input().split())) for i in range(const[0])]

top = const[0]*const[1]
bottom = const[0]*const[1]
left = sum(given[0])
right = sum(given[len(given)-1])
front = 0
back = 0
middle = 0

for i in given:
    val = 0
    for j in i:
        front+= abs(j - val)
        val = j
    back+=j

for a in range(const[1]):
    for b in range(const[0]-1):
        middle+= abs(given[b][a]-given[b+1][a])

sarea = top+bottom+left+right+front+back+middle

print(sarea)