# OOPs Questions Practice...!!

class Dog:
    def __init__(self,n,sc,el,spot):
        self.name =n
        self.skinColor = sc
        self.earLength = el
        self.isSpotted =spot
        print("Dog has been created!!")

    def walk(self):
        print("{0} is walking!".format(self.name))

    def eat(self):
        print("{0} is eating!\n\n".format(self.name))

dog1 = Dog('ScoobyDoo','brown','short',True)  # Creating an object
dog1.walk()
dog1.eat()

dog2 = Dog('Tom','brown','short',True)        # Creating an object
dog1.walk()
dog1.eat()



# *******************************************************************************************



class Myclass:
    x=5
p1 = Myclass()
print(p1.x)
print(Myclass)
print("\n\n\n")



# ************************************************************************************************



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)   # Creating an object
print(p1.name)  # Syntax for printing values of objects
print(p1.age)
print("\n\n")



# ************************************************************************************************


# Other way of printing the values of the objects by using Functions...!!
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
        print("And my age is " + self.age)

p1 = Person("John", "32")
p1.myfunc()  # Other way of printing the values of the objects by using Functions...!!
print("\n\n\n")

# ************************************************************************************************


# Yet another way of defining and printing values using object
class Person:
    def __init__(myobject,name,age):
        myobject.name = name
        myobject.age =age

p1 = Person("Raj", "19")
p1.age = "40"
print(p1.name)
print(p1.age)

del p1.age # After deleting the age property...!!
print(p1.age)
