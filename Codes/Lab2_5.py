#  # generate a program to calculate the sum of odd and even numbers in a list
# # def sum_odd_even(numbers):
# #     odd_sum = 0
# #     even_sum = 0
# #     for num in numbers:
# #         if num % 2 == 0:
# #             even_sum += num
# #         else:
# #             odd_sum += num
# #     return odd_sum, even_sum
# # numbers = [1, 2, 3, 4, 5, 6]
# # odd_sum, even_sum = sum_odd_even(numbers)
# # print(f"Sum of odd numbers: {odd_sum}")
# # print(f"Sum of even numbers: {even_sum}")
# # # justification 
# # # The provided code effectively calculates the sum of odd and even numbers in a list by iterating through each number and checking its parity using the modulus operator. The sums are accumulated in separate variables, which are then returned and printed. This approach is efficient and straightforward, ensuring clarity and ease of understanding. The use of descriptive variable names enhances code readability, making it easy to follow the logic behind the summation process.
# """ improved version of the above code """
# def sum_odd_even(numbers):
#     odd_sum = sum(num for num in numbers if num % 2 != 0)
#     even_sum = sum(num for num in numbers if num % 2 == 0)
#     return odd_sum, even_sum
# numbers = [1, 2, 3, 4, 5, 6]
# odd_sum, even_sum = sum_odd_even(numbers)
# print(f"Sum of odd numbers: {odd_sum}")
# print(f"Sum of even numbers: {even_sum}")
# # """Scenario: You are onboarding a junior developer. explain a function that calculates the area of different shapes
# def calculate_area(shape, dimensions):
#     if shape == "rectangle":
#         length, width = dimensions
#         return length * width
#     elif shape == "circle":
#         radius, = dimensions
#         return 3.14159 * radius * radius
#     elif shape == "triangle":
#         base, height = dimensions
#         return 0.5 * base * height
#     else:
#         raise ValueError("Unsupported shape")
# # Example usage:
# rectangle_area = calculate_area("rectangle", (5, 10))
# circle_area = calculate_area("circle", (7,))
# triangle_area = calculate_area("triangle", (4, 8))
# print(f"Rectangle Area: {rectangle_area}")
# print(f"Circle Area: {circle_area}")
# print(f"Triangle Area: {triangle_area}")
def get_ai_comparison():
    return [
        {
            "name": "Gemini",
            "usability": "High",
            "code_quality": "High",
            "notes": "Strong multi-turn reasoning and context handling; excellent for complex designs, occasional hallucinations."
        },
        {
            "name": "Copilot",
            "usability": "Very High",
            "code_quality": "High",
            "notes": "Seamless IDE integration and inline suggestions; produces idiomatic snippets, may miss edge cases."
        },
        {
            "name": "Cursor AI",
            "usability": "High",
            "code_quality": "Good",
            "notes": "Editor-focused workflows and refactoring tools; fast for edits, less capable on deep reasoning tasks."
        },
    ]

if __name__ == "__main__":
    for item in get_ai_comparison():
        print(f"{item['name']}: usability={item['usability']}, code_quality={item['code_quality']} - {item['notes']}")
