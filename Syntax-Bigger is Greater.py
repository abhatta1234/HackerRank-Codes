
# Given a list of word, print a string that is just greater than it. If the given string cannot be permutated to the
# greater value , print("no answer")


from itertools import permutations
num = int(input())

for i in range(num):
    a = input()

    if len(set(a)) == 1:
        print("no answer")
    elif list(reversed(a)) == list(sorted(a)):
        print("no answer")
    else:
        b = sorted(a)
        c = tuple(a.replace("", " ").split())
        try:
            perm = list(permutations(b))
            indx = perm.index(c)
            print("".join(perm[indx+1]))
        except IndexError:
            print("no answer")