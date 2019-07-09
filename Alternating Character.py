
# Print the number of deletions of characters required each in n strings such that the string doesn't have any adjacent
# same character.

num = int(input())

for i in range(num):
    count = 0
    inp = input()
    for j in range(len(inp)-1):
        if inp[j] == inp[j+1]:
            count+=1
    print(count)