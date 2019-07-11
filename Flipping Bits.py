# You will be given a list of 32 bit unsigned integers. Flip all the bits ( 1 to 0 and 0 to 1) and print the result
# as an unsigned integer.

for i in range(int(input())):
    binary = bin(int(input()))[2:].zfill(32)
    flip = ''.join('1' if x == '0' else '0' for x in binary)
    print(int(flip,2))
