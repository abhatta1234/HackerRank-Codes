# Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help. Letters in some of the SOS
# messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string,s
# determine how many letters of Sami's SOS have been changed by radiation. 

#Algorithm:
inp = input()
pattern = "SOS"
diff = len(inp)-2
count = 0
for i in range(0,diff,3):
    if inp[i:i+3] != pattern:
        if inp[i] != "S":
            count+=1
        if inp[i+1] != "O":
            count+=1
        if inp[i+2] != "S":
            count+=1
print(count)

# Using in-built function to count the number of times the pattern is broken!

inp = input()
pattern = "SOS"
a = inp.count(pattern)
print(len(inp)//3 - a)