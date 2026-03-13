# ===============Q.1===========================
# """ refactor the below code which has multiple repeated code blocks so your task is to 
# identify the duplicate logics and replace it with a function or classes 
# ensure that the refactored code must maintains the same output
# Legacy script with repeated logic
# print("Area of Rectangle:", 5 * 10)
# print("Perimeter of Rectangle:", 2 * (5 + 10))

# print("Area of Rectangle:", 7 * 12)
# print("Perimeter of Rectangle:", 2 * (7 + 12))

# print("Area of Rectangle:", 10 * 15)
# print("Perimeter of Rectangle:", 2 * (10 + 15))
# •	Expected Output:
# o	Refactored code with a reusable function and no duplication.
# o	Well documented code
# docstring for each function and class
#  """
# def calculate_rectangle_properties(length, width):
#     """ Calculate the area and perimeter of a rectangle.
#     Parameters:
#     length (float): The length of the rectangle.
#     width (float): The width of the rectangle.
#     Returns:
#     tuple: A tuple containing the area and perimeter of the rectangle.
#     """
#     area = length * width
#     perimeter = 2 * (length + width)
#     return area, perimeter
# # Testing the function with different rectangle dimensions
# length1, width1 = 5, 10
# area1, perimeter1 = calculate_rectangle_properties(length1, width1)
# print(f"Area of Rectangle: {area1}")
# print(f"Perimeter of Rectangle: {perimeter1}")

#question 2
# """ refactor the code to improve where multiple calculations are embedded directly inside the main code block.
# •	Instructions:
# o	Identify repeated or related logic and extract it into reusable functions.
# o	Ensure the refactored code is modular, easy to read, and documented with docstrings.
# •	Sample Legacy Code:


# # Legacy script with inline repeated logic
# price = 250
# tax = price * 0.18
# total = price + tax
# print("Total Price:", total)

# price = 500
# tax = price * 0.18
# total = price + tax
# print("Total Price:", total)

# •	Expected Output:
# o	Code with a function calculate_total(price) that can be reused for multiple price inputs.
# o	Well documented code
#  """
# # def calculate_total(price):
# #     """ Calculate the total price including tax.
# #     Parameters:
# #     price (float): The original price of the item.
# #     Returns:
# #     float: The total price after adding tax.
# #     """
# #     tax = price * 0.18
# #     total = price + tax
# #     return total
# # # Testing the function with different price inputs
# # price1 = 250
# # total1 = calculate_total(price1)
# # print(f"Total Price: {total1}")


# """ Refactor a Python script that contains repeated if–elif–else grading logic by implementing a structured, object-oriented solution using a class and a method.
# The given script contains duplicated conditional statements used to assign grades based on student marks. This redundancy violates clean code principles and reduces maintainability.
# You are required to refactor the script using a class-based design to improve modularity, reusability, and readability while preserving the original grading logic.
# 4.	Include proper docstrings for:
# The class
# The method (with parameter and return descriptions)
# • Given code:
# marks = 85
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# else:
#     print("Grade C")
# marks = 72
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# else:
#     print("Grade C")

# """
# class GradeCalculator:
#     """ A class to calculate the grade based on student marks. """
    
#     def calculate_grade(self, marks):
#         """ Calculate the grade based on the given marks.
        
#         Parameters:
#         marks (float): The marks obtained by the student.
        
#         Returns:
#         str: The grade corresponding to the marks.
#         """
#         if marks >= 90:
#             return "Grade A"
#         elif marks >= 75:
#             return "Grade B"
#         else:
#             return "Grade C"
# # Testing the GradeCalculator class with different marks
# grade_calculator = GradeCalculator()
# marks1 = 85
# grade1 = grade_calculator.calculate_grade(marks1)
# print(f"Marks: {marks1}, Grade: {grade1}")
# marks2 = 72
# grade2 = grade_calculator.calculate_grade(marks2)
# print(f"Marks: {marks2}, Grade: {grade2}")

# """ refactor the code into functions 
# Instructions:
# o Identify input, processing, and output sections.
# o Convert each into a separate function.
# o Improve code readability without changing behavior.
# • Sample Legacy Code:
# num = int(input("Enter number: "))
# square = num * num
# print("Square:", square)
# • Expected Output:
# o Modular code using functions like get_input(), calculate_square(), and display_result().
# """
# def get_input():
#     """ Get a number input from the user.
    
#     Returns:
#     int: The number entered by the user.
#     """
#     return int(input("Enter number: "))
# def calculate_square(num):
#     """ Calculate the square of a number.
#     Parameters:
#     num (int): The number to be squared.
#     Returns:
#     int: The square of the input number.
#     """
#     return num * num
# def display_result(square):
#     """ Display the result to the user.
    
#     Parameters:
#     square (int): The square of the number to be displayed.
#     """
#     print("Square:", square)
# # Main function to orchestrate the flow
# def main():
#     num = get_input()
#     square = calculate_square(num)
#     display_result(square)
# # Run the main function
# if __name__ == "__main__":
#     main()


""" (Refactoring Procedural Code into OOP Design)
• Task: Use AI to refactor procedural code into a class-based design.
Focus Areas:
o Object-Oriented principles
o Encapsulation
Legacy Code:
salary = 50000
tax = salary * 0.2
net = salary - tax
print(net)
Expected Outcome:
o A class like EmployeeSalaryCalculator with methods and attributes.
"""
# class EmployeeSalaryCalculator:
#     def __init__(self, salary):
#         self.salary = salary  # Encapsulated attribute
#     def calculate_tax(self):
#         """ Calculate the tax based on the salary.
#         Returns:
#         float: The calculated tax amount.
#         """
#         return self.salary * 0.2  # Tax is 20% of the salary
#     def calculate_net_salary(self):
#         """ Calculate the net salary after deducting tax.
#         Returns:
#         float: The net salary after tax deduction.
#         """
#         tax = self.calculate_tax()
#         net_salary = self.salary - tax
#         return net_salary
# # Testing the EmployeeSalaryCalculator class
# employee = EmployeeSalaryCalculator(50000)
# net_salary = employee.calculate_net_salary()
# print(net_salary)  # Output: 40000.0

""" Refactor the following legacy Python code to optimize the search logic:

users = ["admin", "guest", "editor", "viewer"]
name = input("Enter username: ")
found = False
for u in users:
    if u == name:
        found = True
print("Access Granted" if found else "Access Denied)"""
# users = ["admin", "guest", "editor", "viewer"]
# name = input("Enter username: ")
# found = False
# for u in users:
#     if u == name:
#         found = True
# print("Access Granted" if found else "Access Denied")

""" refactor the poorly structured Library Management script that:
•	Contains repeated conditional logic
•	Does not use reusable functions
•	Lacks documentation
•	Uses print-based procedural execution
•	Does not follow modular programming principles
Your task is to refactor the code into a proper format 
1.	Create a module library.py with functions:
o	add_book(title, author, isbn)
o	remove_book(isbn)
o	search_book(isbn)
2.	Insert triple quotes under each function and let Copilot complete the docstrings.
		Task 7 – Refactoring the Library Management System
Problem Statement
You are provided with a poorly structured Library Management script that:
•	Contains repeated conditional logic
•	Does not use reusable functions
•	Lacks documentation
•	Uses print-based procedural execution
•	Does not follow modular programming principles
Your task is to refactor the code into a proper format 
1.	Create a module library.py with functions:
o	add_book(title, author, isbn)
o	remove_book(isbn)
o	search_book(isbn)
2.	Insert triple quotes under each function and let Copilot complete the docstrings.
3.	Generate documentation in the terminal.
4.	Export the documentation in HTML format.
5.	Open the file in a browser.
Given Code 
# Library Management System (Unstructured Version)
# This code needs refactoring into a proper module with documentation.
library_db = {}
# Adding first book
title = "Python Basics"
author = "John Doe"
isbn = "101"

if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")

# Adding second book (duplicate logic)
title = "AI Fundamentals"
author = "Jane Smith"
isbn = "102"

if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")

# Searching book (repeated logic structure)
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
    print("Book not found.")

# Removing book (again repeated pattern)
isbn = "101"
if isbn in library_db:
    del library_db[isbn]
    print("Book removed successfully.")
else:
    print("Book not found.")

# Searching again
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
#     print("Book not found.")"""
# library_db = {}
# def add_book(title, author, isbn):
#     """ Add a book to the library database.
#     Parameters:
#     title (str): The title of the book.
#     author (str): The author of the book.
#     isbn (str): The ISBN number of the book.
#     Returns:
#     str: A message indicating the result of the operation.
#     """
#     if isbn not in library_db:
#         library_db[isbn] = {"title": title, "author": author}
#         return "Book added successfully."
#     else:
#         return "Book already exists."
# def remove_book(isbn):
#     """ Remove a book from the library database using its ISBN.
#     Parameters:
#     isbn (str): The ISBN number of the book to be removed.
#     Returns:
#     str: A message indicating the result of the operation."""
#     if isbn in library_db:
#         del library_db[isbn]
#         return "Book removed successfully."
#     else:
#         return "Book not found."
# def search_book(isbn):
#     if isbn in library_db:
#         return f"Book Found: {library_db[isbn]}"
#     else:
#         return "Book not found."
# # Testing the functions
# print(add_book("Python Basics", "John Doe", "101"))  # Output: Book added successfully.
# print(add_book("AI Fundamentals", "Jane Smith", "102"))  # Output: Book added successfully.
# print(search_book("101"))  # Output: Book Found: {'title': 'Python Basics', 'author': 'John Doe'}
# print(remove_book("101"))  # Output: Book removed successfully.
# print(search_book("101"))  # Output: Book not found.
# """  -
# """
# def fibonacci(n):
#     """ Generate Fibonacci sequence up to the nth number.
#     Parameters:
#     n (int): The limit up to which the Fibonacci sequence is generated.
#     Returns:
#     list: A list containing the Fibonacci sequence up to the nth number.
#     """
#     sequence = []
#     a, b = 0, 1
#     for i in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence
# # Testing the fibonacci function
# print(fibonacci(10))  

""" •	Refactor into is_prime(n) and is_twin_prime(p1, p2).
•	Add docstrings and optimize.
•	Generate a list of twin primes in a given range using AI.
Bad Code Version:
# twin primes bad version
a=11
b=13
fa=0
for i in range(2,a):
 if a%i==0:
  fa=1
fb=0
for i in range(2,b):
 if b%i==0:
  fb=1
if fa==0 and fb==0 and abs(a-b)==2:
 print("Twin Primes")
else:
 print("Not Twin Primes")
"""
def is_prime(n):
    """ Check if a number is prime.
    Parameters:
    n (int): The number to check for primality.
    Returns:
    bool: True if n is prime, False otherwise.
    """
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# def is_twin_prime(p1, p2):
#     """ Check if two numbers are twin primes.
#     Parameters:
#     p1 (int): The first prime number.
#     p2 (int): The second prime number.
#     Returns:
#     bool: True if p1 and p2 are twin primes, False otherwise.
#     """
#     return is_prime(p1) and is_prime(p2) and abs(p1 - p2) == 2
# # Testing the functions
# print(is_twin_prime(11, 13))  # Output: True

# """Refactor the code to determine the Chinese Zodiac sign based on the year input using function get_zodiac(year) and return the zodiac sign instead of printing it directly."""
# def get_zodiac(year):
#     zodiac_signs = [
#         "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
#         "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"
#     ]
#     return zodiac_signs[year % 12]
# year = int(input("Enter year: "))
# zodiac_sign = get_zodiac(year)
# print(f"The Chinese Zodiac sign for the year {year} is: {zodiac_sign}")

""" The current implementation:
•	Mixes logic and input handling
•	Uses redundant variables
•	Does not use reusable functions properly
•	Returns print statements instead of boolean values
•	Lacks documentation
You must refactor the code to follow clean coding principles.
# Harshad Number Checker (Unstructured Version)

num = int(input("Enter a number: "))

temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    temp = temp // 10

if sum_digits != 0:
    if num % sum_digits == 0:
        print("True")
    else:
        print("False")
else:
    print("False")
You must:
1.	Create a reusable function: is_harshad(number)
2.	The function must:
o	Accept an integer parameter.
o	Return True if the number is divisible by the sum of its digits.
o	Return False otherwise.
3.	Separate user input from core logic.
4.	Add proper docstrings.
5.	Improve readability and maintainability.
6.	Ensure the program handles edge cases (e.g., 0, negative numbers).
"""
def is_harshad(number):
    """ Check if a number is a Harshad number.
    A Harshad number is an integer that is divisible by the sum of its digits.
    
    Parameters:
    number (int): The number to check for being a Harshad number.
    
    Returns:
    bool: True if the number is a Harshad number, False otherwise.
    """
    if number <= 0:
        return False  # Harshad numbers are positive integers
    sum_digits = sum(int(digit) for digit in str(number))
    return sum_digits != 0 and number % sum_digits == 0
# Testing the function with different inputs
print(is_harshad(18))  # Output: True
print(is_harshad(19))  # Output: False
print(is_harshad(0))   # Output: False