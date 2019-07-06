
adv = 5
d = 1
numd = int(input())
total = 0
while d <= numd:
    total+=adv//2
    adv = (adv//2) * 3
    d+=1

print(total)

