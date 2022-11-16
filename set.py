#Sets are used to store multiple items in a single variable.A set is a collection which is unordered , unchaneable and  unindexied.
# Set is one of 4 buit in data types in python used to srore collection of data , the other 3 are List,Tuple and Dictionaryt all with different qualities and usage.

thisset = {"apple","banana","cherry"}
print(thisset)

print(len(thisset))

set1 = {"apple","banana","cherry"}
set2 = {1,5,7,9,3}
set3 = {True,False,True}
print(type(set1))

print(set1)
print(set2)
print(set3)

print("-----------------")

thisset = set(("apple","banana","cherry"))
print(thisset)

thisset1 = {"apple","banana","orange","cherry"}
for x in thisset1:
  print(x)

print("banana" in thisset1)

thisset1.add("Papaya")

# Update is basically used to update the current set , use the update() methods

thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)

print("-------------")

