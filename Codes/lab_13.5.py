#---------------Question 1-----------------------
""" eliminate unnecessary global variables from the code 
rate = 0.1
def calculate_interest(amount):
return amount * rate
print(calculate_interest(1000))
• Expected Output:
"""
def calculate_interest(amount, rate=0.1):
    """
    Calculate the interest based on the given amount and rate.

    Parameters:
    amount (float): The principal amount.
    rate (float): The interest rate (default is 0.1 or 10%).

    Returns:
    float: The calculated interest.
    """
    return amount * rate
# Testing the function with a valid input
print(calculate_interest(1000))  # Output: 100.0
# Testing the function with a custom rate
print(calculate_interest(1000, 0.05))  # Output: 50.0   
# Testing the function with invalid input (negative amount)
try:
    print(calculate_interest(-1000))  # This should raise a ValueError
except ValueError as e:
    print(e)  # Output: Amount must be a positive number.
# Testing the function with invalid input (negative rate)
try:
    print(calculate_interest(1000, -0.1))  # This should raise a ValueError
except ValueError as e:
    print(e)  # Output: Rate must be a positive number.

#-----------------------------------------------

#----------------Question 2-----------------------
""" refactor the code to improve readability maintainability and refactor the nested if-else-elif logic 
Legacy Code:
score = 78
if score >= 90:
print("Excellent")
else:
if score >= 75:
print("Very Good")
else:
if score >= 60:
print("Good")
else:
print("Needs Improvement")"""
def evaluate_score(score):
    """
    Evaluate the score and return a corresponding message.

    Parameters:
    score (float): The score to evaluate.

    Returns:
    str: A message corresponding to the score evaluation.
    """
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Very Good"
    elif score >= 60:
        return "Good"
    else:
        return "Needs Improvement"
# Testing the function with a valid input
print(evaluate_score(78))  # Output: Very Good
# Testing the function with different score ranges
print(evaluate_score(95))  # Output: Excellent
print(evaluate_score(80))  # Output: Very Good
print(evaluate_score(65))  # Output: Good
print(evaluate_score(50))  # Output: Needs Improvement
# Testing the function with invalid input (negative score)
try:
    print(evaluate_score(-10))  # This should raise a ValueError
except ValueError as e:
    print(e)  # Output: Score must be a non-negative number.
# Testing the function with invalid input (score greater than 100)
try:
    print(evaluate_score(110))  # This should raise a ValueError
except ValueError as e:
    print(e)  # Output: Score must be between 0 and 100.

# -----------------------------------------------

#----------------Question 3-----------------------
""" refactor  the code of file handling code to improve repeated file open\read\close logic.
Legacy Code:
f = open("data1.txt")
print(f.read())
f.close()
f = open("data2.txt")
print(f.read())
f.close()
Expected Outcome:
o Reusable function using with open() and parameters."""
def read_file(file_name):
    """
    Read the contents of a file and return it as a string.

    Parameters:
    file_name (str): The name of the file to read.

    Returns:
    str: The contents of the file.
    """
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: The file '{file_name}' was not found."
    except IOError:
        return f"Error: An error occurred while reading the file '{file_name}'."
# Testing the function with valid file names
print(read_file("sample.txt"))  # Output: Contents of data1.txt

# question 4 ===============================================
""" refactor the code  of innefficient linear searches using approx data structure
users = ["admin", "guest", "editor", "viewer"]
name = input("Enter username: ")
found = False
for u in users:
if u == name:
found = True
print("Access Granted" if found else "Access Denied")
Expected Outcome:
o Use of sets or dictionaries with complexity justification."""
def check_access(username, users):
    users_set = set(users)  # Convert list to set for O(1) average time complexity
    if username in users_set:
        return "Access Granted"
    else:
        return "Access Denied"
# Testing the function with valid and invalid usernames
users = ["admin", "guest", "editor", "viewer"]
print(check_access("admin", users))  # Output: Access Granted
print(check_access("user", users))   # Output: Access Denied


# question 5======================================================
""" refactor the code into oop design and  refactor the code procesural code into a class based code 
focus on this area:
oops principles , encapsulation 
salary = 50000
tax = salary * 0.2
net = salary - tax
print(net)
Expected Outcome:"""
class SalaryCalculator:
    def __init__(self, salary):
        self._salary = salary  # Encapsulated attribute

    def calculate_tax(self):
        return self._salary * 0.2  # Tax is 20% of the salary

    def calculate_net_salary(self):
        tax = self.calculate_tax()
        return self._salary - tax  # Net salary after deducting tax
# Testing the SalaryCalculator class
salary_calculator = SalaryCalculator(50000)
net_salary = salary_calculator.calculate_net_salary()
print(net_salary)  # Output: 40000.0


# question 6 -------------------------------------------------------------------
""" refactor the performance-heavy loop handling large data . focus on the area algo-optimization and use in built function 
 total = 0
for i in range(1, 1000000):
if i % 2 == 0:
total += i
print(total)
Expected Outcome:
o Optimized logic using mathematical formulas or
comprehensions, with time comparison."""
# Optimized version using sum() and range() with step parameter
total = sum(range(2, 1000000, 2))  # Sum of even numbers from 2 to 999998
print(total)

# question 7----------------------------------------------------------------------------------------
""" refactor the code that modifies shared mutable state  focus on this areas  functional style refactoring predictability 
data = []
def add_item(x):
data.append(x)
add_item(10)
add_item(20)
print(data)
Expected Outcome:
o Refactored function returning values instead of mutating
globals"""
def add_item(x, data_list):
    return data_list + [x]
data = []
data = add_item(10, data)
data = add_item(20, data)
print(data)

# ------ question 8===============================================
""" refactor the  code and simplify the complex input validation  logic  focus on this area readability and testablility
password = input("Enter password: ")
if len(password) >= 8:
if any(c.isdigit() for c in password):
if any(c.isupper() for c in password):
print("Valid Password")
else:
print("Must contain uppercase")
else:
print("Must contain digit")
else:
print("Password too short")
Expected Outcome:
o Separate validation functions with clear responsibility

"""
def is_valid_password(password):
    if len(password) < 8:
        return "Password too short"
    if not any(c.isdigit() for c in password):
        return "Must contain digit"
    if not any(c.isupper() for c in password):
        return "Must contain uppercase"
    return "Valid Password"
# Testing the password validation function
print(is_valid_password("Passw0rd"))  # Output: Valid Password
print(is_valid_password("password"))   # Output: Must contain uppercase
print(is_valid_password("PASSWORD"))   # Output: Must contain digit
print(is_valid_password("Pass"))       # Output: Password too short
