#In this challenge, you will be given a string. You must remove characters until the string is made up of any two
# alternating characters. When you choose a character to remove, all instances of that character must be removed.
# Your goal is to create the find the length of longest string possible that contains just two alternating letters.

string = input()

sub = sorted(list(set(string)))
length = 0

for i in range(len(sub)-1):
    for j in range(i,len(sub)-1):
        check = (sub[i],sub[j+1])
        a = "".join(filter(lambda c: c in check, string))
        loopcheck = 0
        for _ in range(len(a)-2):
            if a[_] == a[_+2]:
                loopcheck+=1
        if loopcheck == len(a)-2:
                length = max(length,len(a))
print(length)