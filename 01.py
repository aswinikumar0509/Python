#insert element in the array
from array import *
arr1 = [1,2,3,3,4,5]

#print(arr1)

def traversal(array):
    for i in array:
        print(i)

traversal([arr1])

def accesing(array,ind):
    if ind > len(array):
        print("This statement is not suitable for the senario")
    return (array[ind])

print("Accessing the element:",accesing(arr1,1))

def searching_element(array,key):
    for i in array:
        if i==key:
            return array.index(key)
    return "The element was not exist in the array"

print("Searchin for the element : ",searching_element(arr1,1))
