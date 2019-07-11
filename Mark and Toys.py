
#Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some.
# There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount
# to spend, and he wants to maximize the number of toys he buys with this money. Given a list of prices and an amount
# to spend, what is the maximum number of toys Mark can buy?


given = list(map(int,input().split()))
arr = list(map(int,input().split()))

arr = sorted(arr)
i = 0
sum = 0

while sum + arr[i] < given[1]:
    sum+=arr[i]
    i+=1
print(i)


