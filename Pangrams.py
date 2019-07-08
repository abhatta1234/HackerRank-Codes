# Check whether the given string is a pangram or not.


inp = input().replace(" ","").lower()

#### Using Algorithm #####

alp = list(map(chr,range(97,123)))
ans = "not pangram"
a = []
for i in inp:
    if i in alp and i not in a:
        a.append(i)
        if len(a) == 26:
            ans = "pangram"
            break
print(ans)

### Using some in-built function ####
if len(set(inp)) == 26:
    print("pangram")
else:
    print("not pangram")

