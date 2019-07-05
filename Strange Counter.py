# A strange counter displays 3 in the first second. Each second the number displayed decreases by 1 until it reaches 1.
# Then, it starts displaying double of what it started the last cycle. Given any second find what is being displayed on
# the counter.

num = int(input())
rep = 3
count = 0
a = 0

while num> count:
    a+=1
    lastrec = count + 1
    count+= rep
    rep = rep*2

start = 3*2**(a-1)
distance = num - lastrec

print(start - distance)