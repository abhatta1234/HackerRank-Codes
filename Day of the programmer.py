
#Day of the Programmer time travel problem


num = int(input())
val = 0

if num>= 1700 and num<=1917:
    if num%4 ==0:
        val = 244
    else:
        val = 243

elif num!= 1918:
    if num%4 == 0 and num%100 == 0:
        if num%400 ==0:
            val = 244
        else:
            val = 243
    elif num%4 ==0 and num%100 != 0:
            val = 244
    else:
        val = 243
else:
    val = 243-13 #1918 is technically a non leap year and the first day is the 14th(so lost 13 days)

day = 256 - val

print(str(day)+"."+"09"+"."+str(num))


