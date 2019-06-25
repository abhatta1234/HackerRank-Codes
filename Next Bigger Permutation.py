
#Next Bigger permutation for a given list of strings


num = int(input())

for _ in range(num):
    a = list(input())
    i = len(a) - 2
    while not (i < 0 or a[i] < a[i + 1]):
        i -= 1
    if i < 0:
        print("no answer")
    else:

        j = len(a) - 1
        while not (a[j] > a[i]):
            j -= 1
        a[i], a[j] = a[j], a[i]  # swap
        a[i + 1:] = reversed(a[i + 1:])

        print("".join(a))