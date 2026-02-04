# def add_numbers(a, b):
#     return a + b

# # Example usage
# num1 = 10
# num2 = 20
# result = add_numbers(num1, num2)
# print(f"The sum of {num1} and {num2} is {result}")
# # Print multiplication tables from 100 to 1
for num in range(100, 0, -1):
    print(f"\nMultiplication table of {num}:")
    for i in range(1, 11):
        print(f"{num} × {i} = {num * i}")
# for num in range(100, 0, -1):
#     print(f"\nMultiplication table of {num}:")
#     for i in range(0, 21):
#         print(f"{num} × {i} = {num * i}")
