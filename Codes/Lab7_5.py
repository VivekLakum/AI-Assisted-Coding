"""Assume you have assigned the following task to debug the following code which has some errors.Analyze the code given below and rectify the errors to get the output"""
#fix: Mutable default argument
# def add_item(item, items=[]):
#     items.append(item)
#     return items
# print(add_item(1))
# print(add_item(2))
"""debug this code and re-write the correct code below"""
# def check_sum():
#     return (0.1 + 0.2) == 0.3
# print(check_sum())
""" debug this code and re-write the correct code below"""
# Bug: No base case
# def countdown(n):
#     if n == 0:
#         return
#     print(n)
#     countdown(n-1)
# countdown(5)

"""debug this code and re-write the corrected code with proper get()method"""
#     # Bug: Accessing non-existing key
# def get_value():
#     data = {"a": 1, "b": 2}
#     return data.get("c", "Key not found")   
# print(get_value())
""" You are a programming assistant. Analyze the following Python code and identify why the loop never ends. fix the code so that output  prints numbers from 0 to 4."""
# def loop_example():
#     i = 0
#     while i < 5:
#         print(i)
#         i += 1

# loop_example()
""" debug this code and re-write the correct code below by Correct unpacking or using _ for extra values.and explain where it occurs and why
"""
# a,b,_ = (1, 2, 3)
# print(a,b)
"""The error occurs because there are three values in the tuple (1, 2, 3) but only two variables (a and b) to unpack them into. To fix this, we can use an underscore (_) as a placeholder for the extra value that we don't need. This way, we can unpack the first two values into a and b, and ignore the third value."""
# """" debug this code by  giving proper indentation and re-write the correct code below  give inline suggestions where necessary"""

# def func():
#     x = 5          # Indent the line to be inside the function
#     y = 10         # Indent the line to be inside the function
#     return x + y   # Indent the line to be inside the function  
# print(func())      # This line is correctly indented outside the function
# """ debug this code by taking correct import module and re-write the correct code"""
# import math
# print(math.sqrt(16))
""" debug this code by Analyze given code where a return inside a loop prevents full iteration.  """
# def total(numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total
# print(total([1,2,3]))
""" debug the given below code by Analyze given code where a variable is used before being defined. 
it must follow the requirements :
fix the bug defining length and width as parameters ans also add 3 asserts test cases"""
# from turtle import width


# def calculate_area(length, width):
#     return length * width

# print(calculate_area(5, 3))
# assert calculate_area(5, 3) == 15
# assert calculate_area(10, 2) == 20
# assert calculate_area(7, 4) == 28
""" debug the given code by Analyze given code where Analyze given code where integers and strings are added incorrectly.I need this requirements in the code •	Fix the code by type conversion (e.g., int("10") or str(5)).
•	Verify with 3 assert cases give in line suggestions where necessary
"""
# def add_values():
#     return 5 + int("10")  # Convert the string "10" to an integer before adding
# print(add_values())

""" debug the given code by giving inline suggestions where necessary and Analyze given code where Analyze given code where a list is concatenated with a string without proper conversion. """
# def combine():
#         return "Numbers: " + str([1, 2, 3])  # Convert the list [1, 2, 3] to a string before concatenating
# print(combine())

""" debug this code by suggesting the inline code and add few test cases"""
# def repeat_text():
#     return "Hello" * 2.5
# print(repeat_text())
# """The error occurs because we cannot multiply a string by a non-integer value (2.5 in this case). To fix this, we can either round the number to the nearest integer or convert it to an integer before multiplying. Here’s the corrected code with inline suggestions and test cases:"""
# def repeat_text():
#     return "Hello" * int(2.5)  # Convert 2.5 to an integer (which will be 2) before multiplying
# print(repeat_text())  # Output: "HelloHello"
# # Test cases
# assert repeat_text() == "HelloHello"  # Test case 1
# assert repeat_text() != "HelloHelloHello"  # Test case 2    
# assert repeat_text() == "HelloHello"  # Test case 3

""" debug this code by suggesting the inline code and add few test cases requirements: •	Run and identify the error.
•	Fix by assigning a default value.
•	Validate using asserts.
"""
# def compute():
#     value = None
#     if value is None:
#         value = 0  # Assign a default value of 0
#     return value + 10

# print(compute())

""" debug this code"""
def sum_two_numbers():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    return int(a) + int(b)

print(sum_two_numbers())
