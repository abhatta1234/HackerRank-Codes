
# Two players are playing the nim game where a players wins if it picks up the last card. Given an array of pile of
# of card, print the winner player. ( First or Second)

arr = list(map(int,input().split()))
count = 0
for i in arr:
    count^=i
if count == 0:
    print("Second")
else:
    print("First")