class myclass :
    x =5
p1 = myclass()
print(p1.x)

class Person :

    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Aswini" , 23)

print(p1.name)
print(p1.age)

class person:
    def __int__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Helo my name is " + self.name)

p1 = person("aswini",23)
p1.myfunc()

class person :

    def __int__(myobject,name,age):
        myobject.name = name
        myobject.age = age

    def myfun(abc):
        print("Hello my name is " + abc.name)

#p1 = person("Aswini",23)
#p1.myfun()

print("__________________")


def myfunc():
    x =300
    print(x)

myfunc()