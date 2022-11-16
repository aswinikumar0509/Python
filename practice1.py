print("--------------- List -----------------")

list = [1,2,3,4,5,6]

for i in list:
    print(i)

print("-------------------")


list1 = [1,2,4,6,8,9]

length = len(list)

for i in range(length):
    print(list1[i])

print("----while---------")

list2 = [1,3,5,7,9]

length = len(list)

i=0

while i < length:
    print(list[i])
    i+=1

print("---------4----------")

list3 = [1,3,5,7,9]

[print(i) for i in list]

print('-------------------enumerate-------------------')

mylist = [1,3,5,7,9]

for i , val in enumerate(mylist):
    print(i , ":",val)

print("---------------------")

a = [1,2,3,4,5]

print(*a)

print("Printing the value using the comma seperated value")

print(*a , sep = ",")

print('Print the value using the next line')

print(*a , sep = "\n")

b = ["Hello","Aswini","Kumar"]

print(' '.join(b))

c = [1,2,3,4,5]
print(' '.join(map(str , c)))

print(type(c))
