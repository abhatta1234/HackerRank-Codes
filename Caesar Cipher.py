
#Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each
# letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front
# of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c

num = int(input())
string = list(input())
incr = int(input())%26

for i in range(len(string)):
    if string[i].isalpha() and string[i].islower():
            if ord(string[i])+incr > 122:
                pos = ord(string[i])+incr - 123 +97
                string[i] = chr(pos)
            else:
                string[i] = chr(ord(string[i])+incr)
    elif string[i].isalpha and string[i].isupper():
            if ord(string[i])+incr > 90:
                pos = ord(string[i])+incr - 91+65
                string[i] = chr(pos)
            else:
                string[i] = chr(ord(string[i])+incr)
print("".join(string))