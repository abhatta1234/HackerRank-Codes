
# A utopian tree has been planted during spring with 1 meter height. Each spring it doubles the height and in spring
#increases the height by 1. Find the height of the tree after n cycles.

n = int(input())

a =1
for i in range(n):
    if a%2 == 0:
        a+=1
    else:
        a=2*a

print(a)