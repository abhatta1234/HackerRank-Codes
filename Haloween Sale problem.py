# Haloween Sale Problem: All games are sold at price p, but every subsequent game is d dollar less. This continues until
# cost becomes less than or equal to m, after which all the game are sold at m dollars. Find the total number of games
#that can be bought for s.


pdms = input().split()
p = int(pdms[0])
d = int(pdms[1])
m = int(pdms[2])
s = int(pdms[3])


def howManyGames(p, d, m, s):
    initial = p
    total = 0
    i = 0
    while initial >= m and total + (p - i * d) < s and s > p:
        total += (p - i * d)
        initial -= d
        i += 1
    while initial < m and total + m <= s:
        total += m
        print(total)
        i += 1
        print(i)
    return i


print(howManyGames(p, d, m, s))