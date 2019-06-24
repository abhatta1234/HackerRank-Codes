
# Taking n of chess board and number of obstacles at index 0 and 1 as input respectively
inp = list(map(int,input().split()))
num = inp[0]

# Taking the initial position of the queen as tuple
pos = tuple(map(int,input().split()))

# Creating an empty array and appending all the block position as tuples in the block array
block =[]
for i in range(inp[1]):
    block.append(tuple(map(int,input().split())))

# This produces all the diagonal paths! But not neccessary to solve the problem.
# a=[]
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         if abs(i-pos[0]) == abs(j-pos[1]) and (i,j) != pos:
#             a.append((i,j))
# print(a)

#Iteration through Eight possible paths.

#Direction Upper Right:
count = 0
for i in range(1,num):
    if pos[0] - i >=1 and pos[1]+i <= num:
        char = (pos[0]-i,pos[1]+i)

        if char not in block:
            count+=1
        else:
            break
    else:
        break

#Direction Upper Left:

for i in range(1,num):
    if pos[0] - i >=1 and pos[1] - i >=1:
        char = (pos[0]-i,pos[1]-i)
        if char not in block:
            count+=1
        else:
            break
    else:
        break

#Direction Lower Right:

for i in range(1,num):
    if pos[0]+i <= num and pos[1]+i <= num:
        char = (pos[0]+i,pos[1]+i)
        if char not in block:
            count+=1
        else:
            break
    else:
        break

# Direction Lower Left:

for i in range(1,num):
    if pos[0]+i <=num and pos[1]-i >=1:
        char = (pos[0]+i,pos[1]-i)
        if char not in block:
            count+=1
        else:
            break
    else:
        break

# Direction Right:

for i in range(1,num):
    if pos[1]+i <=num:
        char = (pos[0],pos[1]+i)
        if char not in block:
            count+=1
        else:
            break
    else:
        break

#Direction Left:

for i in range(1,num):
    if pos[1]-i >=1:
        char = (pos[0],pos[1]-i)
        if char not in block:
            count+=1
        else:
            break
    else:
        break

#Direction UP:

for i in range(1,num):
    if pos[0]-i >=1:
        char = (pos[0]-i,pos[1])
        if char not in block:
            count+=1
        else:
            break
    else:
        break
#Direction Down

for i in range(1,num):
    if pos[0]+i <= num:
        char = (pos[0]+i,pos[1])
        if char not in block:
            count+=1
        else:
            break
    else:
        break

# Printing the count as in the number of times the queen can move.

print(count)





