""" refactor the code into functions 
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