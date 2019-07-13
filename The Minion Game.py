
string  = input()
vowel = 0
const = 0

##This Code is actually forming all substring and checking. We don't need it as it takes a lot of computational time##
for i in range(len(a)):
    for j in range(i,len(a)):
        check = a[i:j+1]
        if check[0] in "AEIOU":
            vowel+=1
        else:
            const+=1
##This Code just Counts the possible substrings##

for i in range(0,len(string)):
    if string[i] in "AEIOU":
        vowel+= len(string)-i
    else:
        const+=len(string)- i
## Comparison Statement for what to print ###

if vowel>const:
    print("Kevin",vowel)
elif const>vowel:
    print("Stuart",const)
else:
    print("Draw")




