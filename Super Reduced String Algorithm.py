string = "aaabccddd"

check = 0

while check == 0:
    a = 0
    for i in range(len(string)):
        try:
            if string[i] == string[i+1]:
                string = string[:i]+string[i+2:]
                a+=1
        except IndexError:
            break
    if a == 0 :
        check+=1

print(string)

