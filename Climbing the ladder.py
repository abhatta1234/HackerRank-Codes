
#DENSE RANKING - CLIMBING THE LADDER PROBLEM



# all user inputs
leadnum = int(input())
leaderboard = sorted(list(set(map(int,input().split()))))
scorenum = int(input())
scoreboard = list(map(int,input().split()))

import bisect

for i in scoreboard:
    print((len(leaderboard) - bisect.bisect(leaderboard, i))+1)

# This two codes don't work for large inputs due to runtime error but are functional
# for _ in scoreboard:
#     leaderboard.append(_)
#     res = sorted(list(set(leaderboard)),reverse=True)
#     print(res.index(_)+1)
#     leaderboard.remove(_)


# for i in scoreboard:
#     a = 0
#     b = 0
#     for j in leaderboard:
#         if i < j and b !=j :
#             a+= 1
#             b = j
#     scoreboard = scoreboard[0:a+1]
#     print(a+1)