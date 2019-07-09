#In this challenge, you will be given a string. You must split it into two contiguous substrings, then determine the
# minimum number of characters to change to make the two substrings into anagrams of one another.

for _ in range(int(input())):
    a = input()
    if len(a)%2 != 0:
        count = -1
    else:
        count = 0
        first_half = list(a[:len(a)//2])
        second_half = list(a[len(a)//2:])
        track = []
        for i in first_half:
            if i in second_half:
                track.append(i)
                second_half.remove(i)
        count = len(a)//2 - len(track)
    print(count)
