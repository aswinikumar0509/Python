# String : Strings in python are surrounded by either single quotation marks, or double quotation marks.
#
# 'hello' is the same as "hello".

print("Hello Python")

a = "hello string in python"
print(a)

a = " Hello in the string in Python"
for i in a :
    print(i)

print(a[0])
print(a[4])

b= " Hello World"
print(b[2:5])

print(b[2:4])

print(b[:5])

print(b[2:])

print(b[-5:-2])


a = "Hello string  Python"
print(a.upper())

print(a.lower())

print(a.strip())

print(a.split())

print(a.replace("H","J"))

a = "Hello"
b = "World"
c = a+b
print(c)

c= a + " " + b
print(c)

age = 21
txt = "Hello ,My name is Aswini , I am "+ str(age)
print(txt)

quality = 3
itemno = 567
price = 49.95

myorder = "I want {} pieces of item {}for {} dollars ."
print(myorder.format(quality,itemno,price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)


