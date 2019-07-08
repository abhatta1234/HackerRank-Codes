
# If the absolute difference between all the adjacent elements in the given string and its reversed string is exactly
#same, then the given string is funny.

loop = int(input())

def check(inp):
    rev = inp[::-1]
    frnt = []
    back = []
    for i in range(len(inp)-1):
        frnt.append(abs(ord(inp[i])-ord(inp[i+1])))
        back.append(abs(ord(rev[i]) - ord(rev[i + 1])))

    if frnt == back:
        return "Funny"
    else:
        return "Not Funny"

for i in range(loop):
    print(check(input()))
