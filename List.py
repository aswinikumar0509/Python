# List : List are used to store multiple items in a single variable

thislist = ["apple" , "banana","cherry"]
print(thislist)
thislist.append(["apple" , "Chery"])
print(thislist)
print(len(thislist))


list1 = ["apple","banana","cherry"]
list2 = [1,5,7,9,3]
list3 = [True,False,True]
print(type(list1))
print(type(list2))
print(type(list3))

list1 = ["apple",34,True,40,"male"]
print(list1)

thislist = ["apple","banana" ,"cherry"]
print(thislist[1])

print(thislist[-1])

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])

print(thislist[-4:-1])

if "apple" in thislist:
    print("yes apple is in the fruit list")

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)

thislist1 = ["apple" ,"mango" , "banana"]
thislist1[1:2] = ["blackcurran","watermelon"]
print(thislist1)

thislist2 = ["apple" ,"mango" , "banana"]
thislist2[1:3] = ["blackcurran","watermelon"]
print(thislist2)

thislist3 = ["apple" , "mango","banana"]
thislist3.insert(2,"watermelon")
print(thislist3)

thislist3 = ["apple" ,"mango" , "banana"]
thislist3.append('orange')
print(thislist3)

thislist1 = ["apple" ,"mango" , "banana"]
thislist1.insert(1,"orange")
print(thislist1)

thislist = ["apple" ,"mango" , "banana"]
tropical = ["orange","chery","kiwi"]
thislist.extend(tropical)
print(thislist)

thislist.remove("orange")
print(thislist)

thislist1 = ["apple" ,"mango" , "banana"]
thislist1.pop(1)
print(thislist1)

thislist4 = ["apple" ,"mango" , "banana"]
thislist4.pop()
print(thislist4)

thislist5=["apple" ,"mango" , "banana","orange"]
#del(thislist5)
print(thislist5)

thislist5=["apple" ,"mango" , "banana","orange"]
for i in range(len(thislist5)):
    print(thislist5[i])


thislis=["apple" ,"mango" ,"banana","chery","kiwi"]
i =0
while i <len(thislis):
     print(thislis[i])
     i = i+1

thislis=["apple" ,"mango" ,"banana","chery","kiwi"]
[print (x) for x in thislis]

fruits = ["apple" ," banana" ,"chery","kiwi" ,"mango"]

newlist = []

for i in fruits :
    if "a" in i:
        newlist.append(i)
print(newlist)

fruits = ["apple" ," banana" ,"chery","kiwi" ,"mango"]

newlist1 = [x for x in fruits if "a" in x]
print(newlist1)

# sorting in list

thislist = ["orange" ,"mango","banana","apple"]
thislist.sort()
print(thislist)

thislist1 = [100,50,65,82,23]
thislist1.sort()
print(thislist1)

thislist = ["orange" ,"mango","apple"]
thislist.sort(reverse=True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

def myfun(n):

    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfun)
print(thislist)

thislist7 = ["banana", "Orange", "Kiwi", "cherry"]
thislist7.sort(key = str.lower)
print(thislist7)

thislist8 = ["banana", "Orange", "Kiwi", "cherry"]
thislist8.sort(key = str.upper)
print(thislist8)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)








