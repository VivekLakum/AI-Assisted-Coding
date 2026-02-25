# # # # -

# # # # """ Explanation of the error:
# # # # The error in the original code is that the loop runs from 1 to n-1, which means it does not include n in the multiplication. 
# # # # The factorial of a number n is the product of all positive integers from 1 to n, so we need to include n in the loop.
# # # # To fix the error, we should change the loop to run from 1 to n (inclusive). This can be done by changing the range to `range(1, n + 1)`.
# # # # Here is the corrected code:"""

# # # # from unittest import result


# # # # def factorial(n):
# # # #     result = 1
# # # #     for i in range(1, n + 1):
# # # #         result = result * i
# # # #     return result

# # # # # Now we can test the corrected code with `factorial(5)`:

# # # # print("Factorial of 5 is:", factorial(5))  # Output should be 120
# # # # #When we run `factorial(5)`, it will calculate 1 * 2 * 3 * 4 * 5, which equals 120. Therefore, the output will be 120, confirming that the corrected code works as expected.




# # # """ assume you are a developer whose task is to improve readability and documentation 
# # # the below code is poorly written:
# # # def calc(a, b, c):
# # # if c == "add":
# # # return a + b
# # # elif c == "sub":
# # # return a - b
# # # elif c == "mul":
# # # return a * b
# # # elif c == "div":
# # # critique the function readability , parameter naming 
# # # rewrite the function with:
# # # descriptive function and parameter names 
# # # complere docstring 
# # # exception handling for division by zero 
# # # consideration of input validation and last test with both valid and invalid inputs      
# # #        """
# # # def calculate(operation, num1, num2):
# # #     """
# # #     Perform a basic arithmetic operation on two numbers.

# # #     Parameters:
# # #     operation (str): The operation to perform. Must be one of "add", "subtract", "multiply", or "divide".
# # #     num1 (float): The first number.
# # #     num2 (float): The second number.

# # #     Returns:
# # #     float: The result of the arithmetic operation.

# # #     Raises:
# # #     ValueError: If the operation is not one of the specified options.
# # #     ZeroDivisionError: If the operation is "divide" and num2 is zero.
# # #     """

# # #     if operation == "add":
# # #         return num1 + num2
# # #     elif operation == "subtract":
# # #         return num1 - num2
# # #     elif operation == "multiply":
# # #         return num1 * num2
# # #     elif operation == "divide":
# # #         if num2 == 0:
# # #             raise ZeroDivisionError("Cannot divide by zero.")
# # #         return num1 / num2
# # #     else:
# # #         raise ValueError("Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'.")
    
# # # # Testing the function with valid inputs
# # # print(calculate("add", 10, 5))        # Output: 15
# # # print(calculate("subtract", 10, 5))   # Output: 5
# # # print(calculate("multiply", 10, 5))   # Output: 50
# # # print(calculate("divide", 10, 5))     # Output: 2.0
# # # # Testing the function with invalid inputs
# # # try:
# # #     print(calculate("divide", 10, 0))  # This should raise a ZeroDivisionError
# # # except ZeroDivisionError as e:
# # #     print(e)  # Output: Cannot divide by zero.  
# # # try:
# # #     print(calculate("mod", 10, 5))     # This should raise a ValueError
# # # except ValueError as e:
# # #     print(e)  # Output: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'.

# # """ Act as a strict Python code reviewer and review the following code for correctness
# # Given this code:
# # def Checkprime(n):
# # for i in range(2, n):
# # if n % i == 0:
# # return False
# # return True
# # Tasks:
# # Quickly verify correctness using sample inputs (2, 3, 4, 9, 11, 1, 0, negatives) and point out any logical issues.
# # List all PEP8 violations (naming, indentation, spacing, structure).
# # Refactor the code to be fully PEP8 compliant:
# # Rename the function
# # Fix indentation and spacing
# # Show the final corrected code.
# # Confirm functionality is preserved after refactoring.
# # """
# # def is_prime(number):
# #     """
# #     Check if a number is prime.

# #     Parameters:
# #     number (int): The number to check for primality.

# #     Returns:
# #     bool: True if the number is prime, False otherwise.
# #     """
# #     if number <= 1:
# #         return False
# #     for i in range(2, int(number**0.5) + 1):
# #         if number % i == 0:
# #             return False
# #     return True
# # # Testing the function with sample inputs
# # test_numbers = [2, 3, 4, 9, 11, 1, 0, -5]
# # for num in test_numbers:
# #     print(f"{num} is prime: {is_prime(num)}")

# """" Optimized Prompt
# Act as a senior Python engineer reviewing code in a real GitHub project.
# Given this function submitted by a teammate:
# def processData(d):
#     return [x * 2 for x in d if x % 2 == 0]
# Do the following:
# Manual review:
# Evaluate readability and naming.,modularity.
# Identify edge cases (non-list input, empty list, non-integer elements, etc.).
# suggest better function and variable names and clarify the function’s purpose.
# Add input validation and proper type hints.
# Suggest how to generalize the function 
# Refactor the code based on the review:
# Provide a clean, production-quality version.
# Include type hints and validation.
# """
# # code:
# from typing import List, Union
# def process_data(data: List[Union[int, float]]) -> List[Union[int, float]]:
#     """
#     Process a list of numbers by doubling the even numbers.

#     Parameters:
#     data (List[Union[int, float]]): A list of integers or floats to be processed.

#     Returns:
#     List[Union[int, float]]: A new list containing the doubled values of the even numbers from the input list.

#     Raises:
#     ValueError: If the input is not a list or contains non-numeric elements.
#     """
#     if not isinstance(data, list):
#         raise ValueError("Input must be a list.")
    
#     processed_data = []
#     for x in data:
#         if not isinstance(x, (int, float)):
#             raise ValueError("All elements in the list must be integers or floats.")
#         if x % 2 == 0:
#             processed_data.append(x * 2)
    
#     return processed_data
# # Testing the function with various inputs
# test_inputs = [
#     [1, 2, 3, 4, 5],          # Mixed integers
#     [0, -2, -3, -4],          # Including zero and negative numbers
#     [1.5, 2.0, 3.5, 4.0],    # Mixed floats
#     [],                       # Empty list
#     "not a list",             # Invalid input type
#     [1, "two", 3]             # List with non-numeric element
# ]
# for test in test_inputs:
#     try:
#         result = process_data(test)
#         print(f"Input: {test} -> Output: {result}")
#     except ValueError as e:
#         print(f"Input: {test} -> Error: {e}")
""" Act as a performance-focused Python engineer.
Given this function:
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
Do the following:
Test this function conceptually with a large input (e.g., range(1_000_000)) and explain why it becomes slow.
Use performance-oriented reasoning to:
Suggest optimizations using Python built-ins and/or better iteration patterns.
Mention alternatives like NumPy (when appropriate) and explain when they help.
Provide an optimized version of the function.
Compare the expected execution time before vs after optimization."""
from typing import List
def sum_of_squares(numbers: List[int]) -> int:
    """
    Calculate the sum of squares of a list of numbers.

    Parameters:
    numbers (List[int]): A list of integers to be processed.

    Returns:
    int: The sum of squares of the input numbers.
    """
    return sum(num ** 2 for num in numbers)
# Testing the optimized function with a large input
import time

large_input = list(range(1_000_000))
start_time = time.time()
result = sum_of_squares(large_input)
end_time = time.time()
print(f"Sum of squares for {len(large_input)} numbers: {result}")
print(f"Execution time: {end_time - start_time:.4f} seconds")

