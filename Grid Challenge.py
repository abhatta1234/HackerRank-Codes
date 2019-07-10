
# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically,ascending.
#Determine if the columns are in alphabetical order, top to bottom. Return Yes if there are, else No!

for i in range(int(input())):
    grid = int(input())
    arr = []
    ans = "YES"
    for i in range(grid):
        given = sorted(list(input()))
        row = len(given)
        arr.append(given)
        print(arr)
    for j in range(grid):
        for k in range(grid-1):
            if arr[k][j] > arr[k+1][j]:
                ans="NO"
                break
        else:
            continue
        break
    print(ans)

