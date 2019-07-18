
# Search if the given 2D array exists in the parent array

import re
from collections import Counter
num = int(input())
for i in range(num):
    col = []
    main = []
    arr = list(map(int,input().split()))
    for i in range(arr[0]):
        main.append(input())
    patt = []
    arr1 = list(map(int,input().split()))
    for i in range(arr1[0]):
        patt.append(input())
    i = 0
    answer = "NO"
    pattern = patt[0]
    for a in main:
        if pattern in a :
            pattern1=pattern[0]
            m = re.finditer(pattern1,a)
            for j in m:
                bound = j.span()
                emp = []
                try:
                    for k in range(i,i+arr1[0]):
                        emp.append(main[k][bound[0]:bound[1]+arr1[1]-1])
                except IndexError:
                    continue
                if emp == patt:
                    answer = "YES"
                    break
        i+=1
        if answer == "YES":
            break
    print(answer)




