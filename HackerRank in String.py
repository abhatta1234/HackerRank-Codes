# Check if the given substring is present in the string. Also, the order of each letter in substring should match the
#order in the given string.

num = int(input())

for i in range(num):
    inp = input()
    pattern = "hackerrank"
    i = 0
    ans = "NO"
    a = []
    for j in inp:
        if pattern[i] == j and i <= len(pattern):
            a.append(j)
            i+=1
            if "".join(a) == pattern:
                ans = "YES"
                break
    print(ans)

