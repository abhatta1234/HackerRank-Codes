
#Given a starting and ending value describing a range of integers, determine number of square integers in the range,
#inclusive of the points. The total number of cases are given by num.

num = int(input())
for i in range(num):
    data = list(map(int,input().split()))
    a = data[0]
    b = data[1]

    if int(a**0.5) != int(b**0.5) or a**0.5 == b**0.5:
        if a**0.5 %1 == 0:
            print(int(b ** 0.5) - int(a ** 0.5)+1)
        else:
            print(int(b**0.5)-int(a**0.5))
    else:
        print(0)