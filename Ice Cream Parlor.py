#Sunny and Johnny like to pool their money and go to the ice cream parlor. Johnny never buys the same flavor that Sunny
# does. The only other rule they have is that they spend all of their money.
#Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

for i in range(int(input())):
    money = int(input())
    num_flv = int(input())
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == money:
                print(i+1,j+1)
                break
