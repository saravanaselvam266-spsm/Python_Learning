'''
Person and Student
Create a Person class with attributes name and age.
Create a subClass Student that inherits from Person  (Hint: use the super keyword in python and use)
Print all attributes through a new method in Student class.

The Shape System
Parent Shape (Shape)
#Initialize with a color (string).
#Implement a method `describe()`- print the current color.
#Implement a method area() that do nothing and just pass the method and comes out.

Child Shape (Circle)
#Inherit from Shape class
#The initializer must accept color (string) and radius (float).
#Override the area() method to calculate and return the area of the circle (3.14 * r * r).
Create a Circle object. Call both describe() and area() and print the results.
Demonstrate what happens if you try to instantiate Shape and call its area(). 

'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def printmessage(self):
        print()


class Student(Person):
    def __init__(self):
        pass
