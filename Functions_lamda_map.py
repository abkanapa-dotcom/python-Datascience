# Anonymous functions
# or
# noName functions

# pq = lambda a,b:a+b
# print(pq(1,2))

# qw = lambda m,n: "Truth" if m>n else "False"
# print(qw(5,9))

# y = input("Enter the Number: ")
# er = lambda y: (print(x+y) for x in y)
# print(er())

# zx = lambda: int(input("Enter the number: ")) **2
# print(zx())
#### 3.The function table(n) prints the table of n?

# 50 Python Function Exercises
# 🔹 Beginner (1–15)
# Write a function to print "Hello, World!".
'''def hello():
    print("Hello World")
hello()'''

# Write a function that takes a name and prints "Hello, <name>!".
'''def hello(name):
    return name
print("Welcome to Hyd ", hello('Abhilash'))
'''
# Write a function that adds two numbers and returns the result.
'''def add(a,b):
    return a+b
print("Addition of two numbers: ", add(11,21))
'''
# Write a function that multiplies three numbers.
'''def mutiply(a,b,c):
    return a*b*c
print("Multiplication of a,b,c is: ", mutiply(1,4,11))
'''
# Write a function that checks if a number is even or odd.
'''def odd_even(num):
    if num %2 != 0:
        status = "odd"
    else:
        status = "even"
    return status
print("Status of the number:", odd_even(int(input("Enter the number: "))))
'''
# Write a function that returns the square of a number.
'''def square(num):
    return num **2
print("Square of a number: ", square(int(input("Enter the Number: "))))
'''
# Write a function that returns the maximum of two numbers.
'''def max_number(x,y):
    return x if x>y else y
print("max of two numbers: ", max_number(98,99))
'''
# Write a function that returns the maximum of three numbers.
'''def max_number(x,y,z):
    geatest=[]
    return x if x>y and x>z else (y if y>z else z)
print("max of two numbers: ", max_number(98,99,101))
'''
# Write a function that returns the length of a string.
'''def string_lengt():
    return len(input("enter the string: "))
length = string_lengt()
print(length)
'''
# Write a function that counts vowels in a string.
'''def vowel_count():
    vowels=['a','e','i','o','u']
    vowel_count=0
    return (vowel_count+1 for char in input("Enter String: ") if char in vowels)
final = vowel_count()
print(final)
'''
# Write a function that reverses a string.
'''def reverse_string():
    return reversed(input("Enter the string: "))
final = "".join(reverse_string())
print(final)
'''
# Write a function that converts Celsius to Fahrenheit.
'''def celcius_farenheit():
    return (int(input("Enter the Celcius: ")) * 9/5) + 32
final = celcius_farenheit()
print(final)'''
# Write a function that calculates the area of a circle.
'''import math
def area_circle():
    return math.pi*((int(input("area of circle: ")))**2)
final = area_circle()
print(final)
'''
# Write a function that returns the factorial of a number.
def factoril():
    fact=1
    numberz = int(input("Ener the Number: "))
        if numberz !=1 or numberz !=0:
            fact= fact*(fact-1)
# Write a function that checks if a number is prime.

# Write a function that sums all numbers in a list.

# 🔹 Intermediate (16–35)
# Write a function that finds the largest number in a list.

# Write a function that finds the smallest number in a list.

# Write a function that returns the average of numbers in a list.

# Write a function that removes duplicates from a list.

# Write a function that checks if a string is a palindrome.

# Write a function that counts words in a sentence.

# Write a function that returns the Fibonacci sequence up to n.

# Write a function that finds the GCD of two numbers.

# Write a function that finds the LCM of two numbers.

# Write a function that converts a list into a dictionary with index as key.

# Write a function that returns the sum of digits of a number.

# Write a function that checks if a year is a leap year.

# Write a function that calculates compound interest.

# Write a function that returns the nth Fibonacci number.

# Write a function that sorts a list without using sorted().

# Write a function that merges two lists.

# Write a function that finds common elements between two lists.

# Write a function that returns unique elements from a list.

# Write a function that counts occurrences of each element in a list.

# Write a function that converts a string to title case.

# 🔹 Advanced (36–50)
# Write a recursive function to calculate factorial.

# Write a recursive function to calculate Fibonacci numbers.

# Write a function that uses a nested function to validate input.

# Write a function that returns another function (closure).

# Write a decorator that logs function calls.

# Write a decorator that measures execution time of a function.

# Write a function that accepts variable-length arguments (*args).

# Write a function that accepts keyword arguments (**kwargs).

# Write a function that uses lambda to square numbers in a list.

# Write a function that uses map() to double numbers in a list.

# Write a function that uses filter() to return even numbers from a list.

# Write a function that uses reduce() to calculate product of numbers.

# Write a function that returns a dictionary of multiple operations (add, subtract, multiply, divide).

# Write a function that uses recursion to flatten a nested list.

# Write a function that implements a simple calculator using nested functions.
