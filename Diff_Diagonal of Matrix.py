
# Code to find the Difference in the diagonals of a Square Matrix


num = int(input())
matrix =[]

for i in range(num):
    data = list(map(int,input().split()))
    matrix.append(data)
sum_d1 = 0
sum_d2 = 0
row = num - 1

if (len(matrix[0])) != num :
    print("The given Matrix is not Square")
else:
    for i in range(num):
        sum_d1+= matrix[i][i]
        sum_d2+= matrix[row][i]
        row = row - 1

print(abs(sum_d1-sum_d2))












