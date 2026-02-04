# """ assume you are a developer working on creating a student information module.
# Your task is to implement the following functionality:
# create a student class with attributes
# name:String
# rollNumber: unique integer  
# branch : string 
# create a method  to display_details to print student information in a proper manner
# i need the user to give inputs for those attributes and create an object of the class and display 
# so  i want the expected output  
# A py class with a __init__ and display_details method and also a sample obj creation and output displayed on console """
# class Student:
#     def __init__(self, name: str, rollNumber: int, branch: str):
#         self.name = name
#         self.rollNumber = rollNumber
#         self.branch = branch

#     def display_details(self):
#         print(f"Student Name: {self.name}")
#         print(f"Roll Number: {self.rollNumber}")
#         print(f"Branch: {self.branch}") 
# # Sample object creation and displaying details
# name = input("Enter student name: ")
# rollNumber = int(input("Enter roll number: "))
# branch = input("Enter branch: ")
# student = Student(name, rollNumber, branch)
# student.display_details()
# # justification 
# # The Student class is designed to encapsulate student information with clear attributes and methods. The __init__ method initializes the object's state, ensuring that each student has a name, roll number, and branch. The display_details method provides a straightforward way to output the student's information in a readable format. By prompting the user for input, we ensure that the class can be used interactively, making it versatile for various applications. This design promotes code organization, readability, and ease of maintenance.
"""Assume you are a developer developing a mode to make the multiples of a number by using python so your task it to:
create a function that takes an interger from user and print the multiples of that number upto 10 multiples using a loop 
for better understanding i want to use the following program with 2  types of loops for loop and while loop and compare the both code  """
# def print_multiples_for_loop(number):
#     print(f"Multiples of {number} using for loop:")
#     for i in range(1, 11):
#         print(f"{number} × {i} = {number * i}")
# def print_multiples_while_loop(number):
#     print(f"Multiples of {number} using while loop:")
#     i = 1
#     while i <= 10:
#         print(f"{number} × {i} = {number * i}")
#         i += 1  
# # Taking input from user
# number = int(input("Enter an integer to print its multiples: "))
# print_multiples_for_loop(number)
# print_multiples_while_loop(number)
# justification
# The provided code defines two functions to print the multiples of a given integer using different looping constructs: a for loop and a while loop. The for loop version is concise and straightforward, iterating over a predefined range to generate multiples. In contrast, the while loop version offers more control over the iteration process, explicitly managing the loop variable. Both approaches effectively achieve the same outcome, demonstrating the versatility of Python's looping mechanisms. This comparison highlights the strengths of each method, allowing developers to choose based on their specific needs and preferences.
# # Comparison of For Loop vs While Loop for Printing Multiples
# comparison_table = """
# ╔══════════════════════════════╦══════════════════════════════╦══════════════════════════════╗
# ║ Aspect                       ║ For Loop                     ║ While Loop                   ║
# ╠══════════════════════════════╬══════════════════════════════╬══════════════════════════════╣
# ║ Readability                  ║ Clear and concise for fixed  ║ Slightly less clear due to    ║
# ║                              ║ iterations                   ║ manual control of loop        ║ 
# ╠══════════════════════════════╬══════════════════════════════╬══════════════════════════════╣
# ║ Control Flow                 ║ Implicit control with range  ║ Explicit control with        ║
# ║                              ║ function                     ║ initialization and increment  ║ 
# ╠══════════════════════════════╬══════════════════════════════╬══════════════════════════════╣
# ║ Use Case                     ║ Best for known iteration     ║ Best for unknown iterations   ║
# ║                              ║ count                        ║ or complex conditions         ║
# ╠══════════════════════════════╬══════════════════════════════╬══════════════════════════════╣
# ║ Performance                  ║ Slightly faster due to less  ║ Slightly slower due to        ║
# ║                              ║ overhead                     ║ additional control logic      ║
# ╠══════════════════════════════╬══════════════════════════════╬══════════════════════════════╣
# ║ Error-Prone                  ║ Less prone to infinite loops ║ More prone to infinite loops   ║
# ║                              ║ due to fixed iteration count  ║ if not properly managed       ║        
# ╚══════════════════════════════╩══════════════════════════════╩══════════════════════════════╝
# """
# print(comparison_table)
# justification
# The comparison table highlights the key differences between using for loops and while loops for printing multiples of a number. For loops offer better readability and are ideal for scenarios with a known iteration count, making them less error-prone. In contrast, while loops provide more control and flexibility for complex conditions but require careful management to avoid infinite loops. Performance differences are minimal, but for loops generally have a slight edge due to reduced overhead. Overall, the choice between the two depends on the specific use case and developer preference.
""" assume you  are a developer working on creating a module to compare for loop and while loop in python 
so your task is to  implement the following functionality:
# create a function that takes an integer from user 
# you need to calculate the 1st sum of n natural numbers using for loop and while loop both and compare the both code
# First i want to excute the code using for loop and then using while loop and then compare the both code  """
def sum_natural_numbers_for_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
def sum_natural_numbers_while_loop(n):
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total
# Taking input from user
n = int(input("Enter a positive integer to calculate the sum of first n natural numbers: "))
sum_for_loop = sum_natural_numbers_for_loop(n)  
sum_while_loop = sum_natural_numbers_while_loop(n)
print(f"Sum of first {n} natural numbers using for loop: {sum_for_loop}")
print(f"Sum of first {n} natural numbers using while loop: {sum_while_loop}")
# justification