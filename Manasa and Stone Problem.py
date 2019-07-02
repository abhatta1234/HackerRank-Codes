
#Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail
# and notices that any two consecutive stones' numbers differ by one of two values. Legend has it that there is a
# treasure trove at the end of the trail. If Manasa can guess the value of the last stone, the treasure will be hers.

#Manasa and Stones Problem:

for i in range(int(input())):
    n = int(input())
    a = int(input())
    b = int(input())
    list = []
    j=0
    for i in range(n):
        sum = i*a+(n-1-i)*b
        if sum not in list:
            list.append(sum)
    print(*sorted(list))