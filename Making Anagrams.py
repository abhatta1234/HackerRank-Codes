
# Given two strings,s1 and s2, that may not be of the same length, determine the minimum number of character deletions
# required to make s1 and s2 anagrams. Any characters can be deleted from either of the strings.

string1 = input()
string2 = input()

if len(string1) > len(string2):
    loop = list(string1)
    non_loop = list(string2)
else:
    loop = list(string2)
    non_loop = list(string1)
track = []

for i in loop:
    if i in non_loop:
        track.append(i)
        non_loop.remove(i)

print(len(string1)+len(string2)-2*len(track))

