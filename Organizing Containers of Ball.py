
num = int(input())

for i in range(num):
    cont = int(input())
    col = []
    sum_set = []
    for i in range(cont):
        arr = list(map(int,input().split()))
        col.append(arr)
        sum_set.append(sum(arr))
    sum_ith = list(map(sum,zip(*col)))
    ## sun_set = [sum(i) for i in col] ## Can use this to get sum but just appended sum while taking input.
    print(sum_ith)
    print(sum_set)
    if sorted(sum_ith) == sorted(sum_set):
        print("Possible")
    else:
        print("Impossible")


