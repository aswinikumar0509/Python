l = [1,3,4,5,5]
for i in l:
   print(i)

b= iter(l)
next(b)
next(b)

print("++++++++++++++++++++++")

s="aswini"
for i in s:
    print(i)

print("++++++++++++++++")

t = (5,6,7,8,9)
for i in t:
    print(i)
#iterable
#iterator

# generator function are the function iterate when we call the function.

list(range(1,10))

def squ(n):
    x = [i*i for i in range(n)]
    yield x

print(squ(4))

def my_function():
    print("Hello from the function")

my_function()

def my_function(fun_name):

    print(fun_name+" " +"Refsnes")

my_function("Email")
my_function("aswini")
my_function("kumar")

def my_function(fname,lname):
    print(fname+" "+lname)

my_function('email',"refsnes")

def my_function(*kids):
    print("The youngest child is " + kids[1])

my_function('email',"aswini","kumar")


def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fun_name = "aswini",lname = "kumar")


def my_function(country = "Norway"):
    print("I am from " + country)

my_function("India")
my_function("USA")
my_function()
my_function("China")

def my_function(food):

    for x in food:
        print(x)

fruits = ["apple","banana","orange","cherry"]
my_function(fruits)


def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(8))
print(my_function(9))

def myfunction():
    pass

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\nresult")
tri_recursion(6)



def myfunc():
    x =300
    print(x)

myfunc()


def myfunc():

    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()


x=200

def myfunc():
    print(x)

myfunc()

print(x)

x = 300

def myfunc():
    x =200
    print(x)

myfunc()

print(x)

def myfunc():
    global x
    x =300

    myfunc()

print(x)

x = 300
def myfunc():
    global x
    x =200

myfunc()
print(x)

def greeting(name):
    print("Hello , " + name)








