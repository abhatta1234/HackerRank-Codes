
# Given a range of number. Print if any kaprekar number exists. Kaprekar number are those numbers, whose squares splitted
# into two and added should give the same number . Eg: 9**2 = 81: 8+1 = 9

start = int(input())
end = int(input())
col = []
for i in range(start,end+1):
    val = str(i**2)
    span = len(val)
    span1 = span//2
    first = val[:span1]
    second = val[span1:]
    if first:
        total = int(first) + int(second)
    else:
        total = int(second)

    if i == total:
            col.append(i)
if col:
    print(*col)
else:
    print("INVALID RANGE")


