# """write a python code for leap year checking.the function should be accepting a year form user,checks whether the given year is a leap year or not """
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# print("\n" + "="*60)
# print("COMPARISON TABLE")
# print("="*60)
# comparison = """

# ║ Readability        ║ Verbose            ║ Concise, Pythonic  ║
# ╠════════════════════╬════════════════════╬════════════════════╣
# ║ Large Inputs       ║ Slow, inefficient  ║ Fast, optimized    ║
# ╠════════════════════╬════════════════════╬════════════════════╣
# ║ Educational Value  ║ Great for learning ║ Practical, modern  ║    
# ╠════════════════════╬════════════════════╬════════════════════╣
# ║ When to Use        ║ Learning/Teaching  ║ Production code    ║        
# ║                    ║ Understanding      ║ Real-world apps    ║
# ║                    ║ string mechanics   ║ Performance-critical║
# ╚════════════════════╩════════════════════╩════════════════════╝
# """
# print(comparison)

# # write a python code for leap year checking.the function should be accepting a year form user,checks whether the given year is a leap year or not 
# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
# # Example usage
# year = int(input("Enter a year: "))
# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# write a python code for converting centimeters to inches by using mathematical formula.example when user gave input 10cm and output should be 3.93 inches
# def cm_to_inches(cm):
#     inches = cm / 2.54
#     return inches
# # Example usage
# cm_value = float(input("Enter length in centimeters: "))
# inches_value = cm_to_inches(cm_value)
# print(f"{cm_value} cm is equal to {inches_value:.2f} inches.")
# # write a python code for name formating function that accepts first name and last name from user and returns the full name as "Last Name, First Name" example input : first name = john , last name = smith output : smith, john  example 2: first name =  anitha , last name =  Rao output : Rao, Anitha
# def format_name(first_name, last_name):
#     return f"{last_name.capitalize()}, {first_name.capitalize()}"
# # Example usage
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# formatted_name = format_name(first_name, last_name)
# print(f"Formatted Name: {formatted_name}")

# Write a function in Python that takes a string as input and returns the number of vowels in the string. Consider both uppercase and lowercase vowels.
# def count_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     count = sum(1 for char in input_string if char in vowels)
#     return count
# # Example usage
# user_string = input("Enter a string: ") 
# vowel_count = count_vowels(user_string)
# print(f"Number of vowels in the string: {vowel_count}")
# Example 1:Input: "apple"Output: 2 Example 2:Input: "HELLO"Output: 2 Now write a Python function that takes a string as input and returns the number of vowels in it.Count both uppercase and lowercase vowels.
# def count_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     count = sum(1 for char in input_string if char in vowels)
#     return count
# # Example usage
# user_string = input("Enter a string: ")
# vowel_count = count_vowels(user_string)
# print(f"Number of vowels in the string: {vowel_count}")
""" Example 1:
File content (sample1.txt):
Hello
Welcome to Python
File handling example
Output:
Number of lines = 3
Example 2:
File content (sample2.txt):
This is line one
This is line two
Output:
Number of lines = 2
Now write a Python function that:
• Reads a .txt file
• Counts the total number of lines in the file
• Returns the line count"""
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count
    except FileNotFoundError:
        return "File not found. Please check the file path."

