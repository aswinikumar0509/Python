import numpy as np

twoDArray = np.array([[11,21,31],[10,14,15],[11,21,21],[16,14,36]])
print(twoDArray)

# Insertation of the columns in two dimentional array

newtwoArray = np.insert(twoDArray,0,[[32,45,67]],axis=0)
print(newtwoArray)

# Access element in twoDArray

def accessElement(array , rowindex,columnindex):
    if rowindex >= len(array) and columnindex >= len(array[0]):
        print("Incorrete index")
    else:
        print(array[rowindex][columnindex])

accessElement(newtwoArray,1,2)

# Traversing the two-D Array

def traverseTDarray(array):
    for i in range (len(array)):
        for j in range (len(array[0])):
            print(array[i][j])

traverseTDarray(twoDArray)

# Search the given value inside the twoDarray

def searchelement(array,value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]== value:
                return "The value in the location "+str(i)+" "+str(j)
    return "Value not found "

print(searchelement(twoDArray,31))

a = [1,2,3,4,5]
print(a[3:0:-1])

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6):
    print(arr[i], end = " ")
print("-------------------")
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])

a=[1,2,3,4,5,6,7,8,9]
print(a[::2])


print("--------------------------")

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v


print(fun(data[0]))
