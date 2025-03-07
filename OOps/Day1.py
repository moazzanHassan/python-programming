# how to define a class
# 🎯 Day 1 Tasks
# ✅ Task 1: Create a class Laptop with attributes brand, model, and price, then create an object and print its details.
class car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

my_car = car("Tyota","mix")

# print(my_car.brand)
# Task 1
class Laptop:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    
laptop1 = Laptop("Dell","Latitude 7480",48000)
# print(laptop1.brand,laptop1.model,laptop1.price)
# ✅ Task 2: Modify the Car class to include a drive() method that prints "The car is moving".
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute
        self.model = model
        self.year = year
    def drive(self):
        return ("The car is moving")

# Creating an Object (Instance)
my_car = Car("Toyota", "Corolla", 2022)

# Accessing Attributes
print(my_car.drive())
# ✅ Task 3: Create a Student class with attributes name, grade, and school, and a method get_details() to return a formatted string.
class Student:
    def __init__(self,name,grade,school):
        self.name = name
        self.grade = grade
        self.school = school
        
    def get_details(self):
        return (f"my name is {self.name}. my grades are {self.grade}.my school name is {self.school}")

Student1 = Student("ghafar","A+","nasreen public school")
Student2 = Student("zaheer","A+","wazi public school")

# print(Student1.get_details())
# print(Student2.get_details())