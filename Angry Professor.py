
# A professor decides that if less than a given number of student are not present at the start of the class
# , the class will be cancelled. Find if class was cancelled. 


num = int(input())

for i in range(num):
    cstr = list(map(int,input().split()))
    stdn = list(map(int,input().split()))

    if len([_ for _ in stdn if _ <= 0]) >= cstr[1]:
        print("NO")
    else:
        print("YES")
