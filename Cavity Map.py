# You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth.
# We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell
# adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side, or edge.
# Find all the cavities and replace their depth with uppercase letter X.

n = int(input())
arr = []
new_arr = []
for i in range(n):
    arr.append(list((input().strip())))
new_arr = arr.copy()
for i in range(1,n-1):
    for j in range(1,n-1):
        if arr[i][j] > arr[i][j+1]:
            if arr[i][j]>arr[i][j-1]:
                if arr[i][j] > arr[i-1][j]:
                    if arr[i][j]>arr[i+1][j]:
                        new_arr[i][j] = "X"
for i in new_arr:
    print(*i,sep="")




