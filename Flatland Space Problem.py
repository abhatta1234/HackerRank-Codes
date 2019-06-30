# Flatland is a country with a number of cities, some of which have space stations. Cities are numbered consecutively
# and each has a road of 1km length connecting it to the next city. It is not a circular route, so the first city
# doesn't connect with the last city. Determine the maximum distance from any city to it's nearest space station.

inp1 = list(map(int,input().split()))
arr = sorted(list(map(int,input().split())))
val = 0
for i in range(len(arr)-1): # Find the max distance between the city with in the array
    val = max(val,abs(arr[i+1]-arr[i]))
val = val - 1
if val%2 ==0:
    val = val//2
else:
    val = val//2+1
start = arr[0]-0 # Find the distance before first station if any
end = (inp1[0]-1)- arr[len(arr)-1] # Find the distance after last station if any

print(max(val,end,start))



