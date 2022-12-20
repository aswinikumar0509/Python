from array import *

# Create an array and traverse

my_array = array('i',[1,2,3,4,5])

for i in my_array:
    print(i)

# 2 Asscessing the given element
print(my_array[3])

# Append the element in the array

my_array.append(6)
print(my_array)

# Insert value in the array using insert method
print("Step-4")
my_array.insert(0,11)
print(my_array)

# Extend method for the
print("step-5")
my_array1 = array('i',[10,11,12])
my_array.extend(my_array1)
print(my_array)

# Add items from list into array using from list() method
print("step6")
temp_list = [20,21,22]
my_array.fromlist(temp_list)
print(my_array)

# Remove the array element using remove method
print("step7")
my_array.remove((11))
print(my_array)

# Remove last array by using pop method
print("step8")
my_array.pop()
print(my_array)

#Fetch any element through its index using index method
print("step9")
print(my_array.index(21))

# reverse method for the array
print("step10")
my_array.reverse()
print(my_array)

# Get array buffer information through the buffer information
print("Step11")
print(my_array.buffer_info())

# Check the number of the element occurance of the element using count method
print("Step12")
my_array.append(11)
print(my_array.count(11))

# Converting array to string using to_string method

# Converting array ro list
print("step14")
#print(my_array.tolist())

# Slice the array
print("step15")
print(my_array[1:4])