
# Change all the given string to palindromes. To do so: you can reduce the value of letter by 1 ( d to c, not c to d)
# and letter a may not be reduced further. Find the minimum number of operations required to convert a string into
# a palindrome.

num = int(input())
for i in range(num):
    a = input()
    rev = a[::-1]
    count = 0
    for i in range(len(a)//2):
        count+= abs(ord(rev[i])- ord(a[i]))
    print(count)
