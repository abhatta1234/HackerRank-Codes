
house = list(map(int,input().split()))
tree = list(map(int,input().split())) #location of tree
num= list(map(int,input().split()))  #number of apples or oranges
app = list(map(int,input().split()))  # apple fall
org = list(map(int,input().split()))  #orange fall


# making to array for apple
appl =[]
num_app =[]
for a in app:
    appl.append(a+tree[0])

for i in appl:
    if i in range(house[0],house[1]+1):
        num_app.append(i)

#making array for orange
orgn =[]
for b in org:
    orgn.append(b+tree[1])

num_org = []

for j in orgn:
    if j in range(house[0],house[1]+1):
        num_org.append(j)


print(len(num_app))
print(len(num_org))


