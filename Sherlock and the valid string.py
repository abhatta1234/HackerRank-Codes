from collections import Counter
ans = "NO"
chr = input()

count = Counter(chr)
print(count)

ls = {v:0 for k,v in count.items()} # Creating a dictionary to find the frequency of repetition.

for k,v in count.items():
    ls[v]+=1

if len(ls) == 1: # if all the items is repeated the same time
    ans ="YES"
elif len(ls) == 2 and ls[max(ls.keys())] == 1 and max(ls.keys())-min(ls.keys()) == 1: # if all except one is repeated same time and the different one is repeated just once.
    ans = "YES"
elif len(ls) == 2 and ls[min(ls.keys())] == 1: # if all except one is repeated same time and the different one has only one character.
    ans = "YES"

print(ans)