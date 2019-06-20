
# Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of
#divisors occuring in the integer


n = int(input())
a = map(int,str(n))
count = 0

for i in a:
    try:
        if n % i == 0:
            count += 1
    except ZeroDivisionError:
        count += 0

print(count)