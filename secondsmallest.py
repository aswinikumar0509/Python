import math

arr = [10,13,17,11,34,21]
first = second = math.inf

for i in range(0,len(arr)):
    if arr[i]<first:
        second = first
        first = arr[i]
    elif (arr[i] < second and arr[i]!=first):
        second = arr[i]

print(second)