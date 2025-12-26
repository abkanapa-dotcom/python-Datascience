'''
#properties of bottle
id=1
color='red'
capacity=1
height = 10
def wash():
    print("washing")
def setCap():
    print("setCap")
def fillWater():
    print("fillWater")

class Bottle:
    #properties
    id=1
    color='red'
    capacity=1
    height = 10
    #constructor
    def __init__(self,color,capacity):
        self.color=color
        self.capacity = capacity
        print('constructor')
    #functions
    def wash(self):
        print(self)
        print("washing")
    def setCap():
        print("setCap")
    def fillWater():
        print("fillWater")
#creating object
bottle_1 = Bottle('green',2)
bottle_2 = Bottle('yellow',3)
print(Bottle.capacity)
print(Bottle.id)
print(Bottle.color)
print(Bottle.height)
print(bottle_1)
print(bottle_1.color)
print(bottle_2.color)
bottle_1.wash()
print(bottle_1.id)
print(bottle_2.capacity)
print(bottle_2.height)
'''

'''
Level 1: Very Basic (Understanding Classes & Objects)

Student Class
Create a Student class with attributes name and age. Create one object and display its details.
'''
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
    
object1=Student('Abhilash',40)
object1.Details()

'''
Car Class
Create a Car class with attributes brand and model. Create two objects and print their values.
'''
class Car:
    def __init__(self):
        pass
    def Brand(self,brand):
        print("Name of the car Brand is : ", brand)
        return ""
    def Model(self,model):
        print("Name of the car Model is : ", model)
        return ""
object2 = Car()
object3=Car()
print(object2.Brand("KIA"))
print(object3.Model("2025"))

'''
Book Class
Create a Book class with attributes title and author. Add a method to display book details.
'''
class Book:
    def __init__(self):
        pass
    def bookDetails(self,author,title):
        print(f"The Author is {author}, and the title is {title}")
object4=Book()
object4.bookDetails("'steve hawking'","'A road for a walk'")
'''
Person Class
Create a Person class with attributes name and city. Create an object and print where the person lives.
'''

class Person:
    def __init__(self,city):
        self.city = city
        print(f"Iam living in {city} city right now")
object5 = Person("Oklahoma")
#print(object5) 
'''
Mobile Class
Create a Mobile class with attributes company and price. Create an object and display the details.
'''

class Mobile:
    def __init__(self,company,price):
        self.company = company
        self.price=price
object6=Mobile("Motorola", 36999)
print(f"The {object6.company} phone i use is {object6.price}")
    
'''
🟡 Level 2: Constructors (__init__) and Methods

Employee Class
Create an Employee class with name and salary. Use a constructor to initialize values.
'''
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def employeeDetails(self):
        print(f"My name is {self.name}, and my income is {self.salary}")
object7=Employee("Abhilash", '80LPA')
print(object7.name, object7.salary)
print (object7.employeeDetails())


'''
Rectangle Class
Create a Rectangle class with length and width. Add a method to calculate area.

'''
class Rectangle:
    def __init__(self):
        pass
    def area_rectangel(self,length,width):
        area_of_rectangle = length*width
        return area_of_rectangle
    
object8 = Rectangle()
print(object8.area_rectangel(20,22))


'''
Circle Class
Create a Circle class with radius. Add a method to calculate circumference.

BankAccount Class
Create a BankAccount class with account_holder and balance. Add a method to display balance.

Laptop Class
Create a Laptop class with brand and ram. Add a method to upgrade RAM.
'''
class Laptop:
    def __init__(self):
        pass
    def upgradeRAM(self,performance):
        if performance == 'slow':
            print("Upgrade the RAM in LAPTOP")
        else:
            print("No ned of upgrade of RAM")

object8 = Laptop()
print(object8.upgradeRAM('slow'))

'''
🟠 Level 3: Multiple Methods & Simple Logic

Calculator Class
Create a class with methods for addition, subtraction, multiplication, and division.

Dog Class
Create a Dog class with name and breed. Add a method bark() that prints a message.

Movie Class
Create a Movie class with name, rating, and year. Add a method to check if the movie is a hit (rating ≥ 8).

Account Class
Create an Account class with account_number and balance. Add methods to deposit and withdraw money.

Temperature Class
Create a class that converts Celsius to Fahrenheit.

🔵 Level 4: Object Interaction & Practice

School Class
Create a School class and a Student class. Store student objects inside the school.
'''
class School:
    def __init__(self,school_name):
        self.school_name = school_name
        if school_name == "International":
            class Student1:
                def __init__(self,medium='English'):
                    self.medium = medium
                    print(f"The school Name is {school_name} and medium is {medium}")
        else:
            class Student2:
                def __init__(self,medium='Telugu'):
                    self.medium = medium
                    print(f"The school Name is {school_name} and medium is {medium}")

object9=School("International")
print(object9)

'''
Library Class
Create a Library class that stores book objects and displays all books.

ShoppingCart Class
Create a class that adds items and calculates total price.
'''
class shoppingCart:
    def __init__(self):
        self.items=[]
        
    def add_items(self,item,price):
        self.items.append(price)

    def total_price(self):
        total = sum(self.items)
        print("Total Price: ", total)
cart = shoppingCart()
cart.add_items('book',200)
cart.add_items('shampoo',150)
cart.add_items('water',50)

cart.total_price()

'''

Quiz Class
Create a Quiz class that stores questions and checks answers.

Attendance System
Create a Student class and an Attendance class to mark and display attendance.
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print("Title:", self.title, " Author:", self.author)


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []  # list to store Book objects

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Library Name:", self.library_name)
        for book in self.books:
            book.display_book()


# Create Book objects
b1 = Book("Python Basics", "John Doe")
b2 = Book("OOP Concepts", "Jane Smith")
b3 = Book("Data Science", "Alan Brown")

# Create Library object
library = Library("City Library")

# Add books to the library
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

# Display all books
library.display_books()
