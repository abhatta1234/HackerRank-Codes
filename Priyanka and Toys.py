
# Priyanka works for an international toy company that ships by container. Her task is to the determine the lowest cost
# way to combine her orders for shipping. She has a list of item weights. The shipping company has a requirement that
# all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item.
# All items meeting that requirement will be shipped in one container. Find the Smallest number of container required!

num = int(input())
a = sorted(list(map(int,input().split())))
i = 0
count = 0
min = a[i]
while i < len(a)-1:
    if a[i+1] > min +4:
        min = a[i+1]
        count += 1
    i+=1
print(count+1)



