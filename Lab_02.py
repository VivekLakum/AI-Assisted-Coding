import time

# # # write a python code  to reverse a string which should take input from user and don't use any user defined functions. 
# # while True:
# #     choice = input("Do you want to reverse another string? (yes/no): ")
# #     if choice.lower() != 'yes':
# #         break
# #     a = input("Enter a string: ")
# #     reversed_string = ""
# #     for char in a:
# #         reversed_string = char + reversed_string
# #     print("Reversed string is:", reversed_string)
# #generate code by removing unnecessary variables, simplifying loops and indexing logic, and improving overall readability and efficiency without changing the output
# # a = input("Enter a string: ")
# # reversed_string = ""
# # for char in a:
# #     reversed_string = char + reversed_string
# # print("Reversed string is:", reversed_string)   

# # def reverse_string(s):
# #     return s[::-1]

# # a = input("Enter a string: ")
# # print("Reversed string is:", reverse_string(a))


# # Comparison of String Reversal Approaches

# comparison_table = """
# ╔════════════════════════╦═══════════════════════════╦═══════════════════════════╗
# ║ Aspect                 ║ Without Functions         ║ With User-Defined Functions║
# ╠════════════════════════╬═══════════════════════════╬═══════════════════════════╣
# ║ Code Clarity           ║ Linear, easy to follow    ║ Clear intent, self-documenting
# ║                        ║ for simple tasks          ║ through function name      
# ╠════════════════════════╬═══════════════════════════╬═══════════════════════════╣
# ║ Reusability            ║ Code duplication if used  ║ Single definition, multiple
# ║                        ║ multiple times            ║ calls reduce redundancy   
# ╠════════════════════════╬═══════════════════════════╬═══════════════════════════╣
# ║ Ease of Debugging      ║ Harder to isolate bugs    ║ Easier to test and debug
# ║                        ║ in larger codebases       ║ specific functionality    
# ╠════════════════════════╬═══════════════════════════╬═══════════════════════════╣
# ║ Maintainability        ║ Changes needed in         ║ Update logic in one place
# ║                        ║ multiple locations       ║ affects all usages        
# ╠════════════════════════╬═══════════════════════════╬═══════════════════════════╣
# ║ Testability            ║ Difficult to unit test    ║ Easy to test with different
# ║                        ║ isolated logic            ║ inputs systematically     
# ╠════════════════════════╬═══════════════════════════╬═══════════════════════════╣
# ║ Large-Scale Apps       ║ Not suitable; leads to    ║ Highly suitable; promotes
# ║                        ║ spaghetti code            ║ modularity and scalability
# ╠════════════════════════╬═══════════════════════════╬═══════════════════════════╣
# ║ Memory Efficiency      ║ Code repeated in memory   ║ Single definition in memory
# ║                        ║ multiple times            ║ with multiple references  
# ╚════════════════════════╩═══════════════════════════╩═══════════════════════════╝
# """

# print(comparison_table)

# # Summary
# print("\n✓ Recommendation: Use user-defined functions for production code")
# print("✓ Use without functions: Learning, prototyping, or very simple scripts")
# Implementation 1: Using a loop
def reverse_with_loop(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

# Implementation 2: Using slicing
def reverse_with_slicing(s):
    return s[::-1]

# Test both implementations
test_string = "Hello, World!"
print("Original string:", test_string)
print("Reversed (Loop):", reverse_with_loop(test_string))
print("Reversed (Slicing):", reverse_with_slicing(test_string))

# Performance comparison on large input
large_string = "a" * 100000

# Time loop approach
start = time.time()
for _ in range(100):
    reverse_with_loop(large_string)
loop_time = time.time() - start

# Time slicing approach
start = time.time()
for _ in range(100):
    reverse_with_slicing(large_string)
slicing_time = time.time() - start

print("\n" + "="*60)
print("PERFORMANCE COMPARISON (100,000 character string, 100 iterations)")
print("="*60)
print(f"Loop approach:    {loop_time:.4f} seconds")
print(f"Slicing approach: {slicing_time:.4f} seconds")
print(f"Slicing is {loop_time/slicing_time:.1f}x faster")

print("\n" + "="*60)
print("COMPARISON TABLE")
print("="*60)
comparison = """
╔════════════════════╦════════════════════╦════════════════════╗
║ Aspect             ║ Loop Approach      ║ Slicing Approach   ║
╠════════════════════╬════════════════════╬════════════════════╣
║ Time Complexity    ║ O(n²)              ║ O(n)               ║
║ (string concat)    ║ (string immutable) ║ (optimized)        ║
╠════════════════════╬════════════════════╬════════════════════╣
║ Space Complexity   ║ O(n)               ║ O(n)               ║
╠════════════════════╬════════════════════╬════════════════════╣
║ Readability        ║ Verbose            ║ Concise, Pythonic  ║
╠════════════════════╬════════════════════╬════════════════════╣
║ Large Inputs       ║ Slow, inefficient  ║ Fast, optimized    ║
╠════════════════════╬════════════════════╬════════════════════╣
║ Educational Value  ║ Great for learning ║ Practical, modern  ║
╠════════════════════╬════════════════════╬════════════════════╣
║ When to Use        ║ Learning/Teaching  ║ Production code    ║
║                    ║ Understanding      ║ Real-world apps    ║
║                    ║ string mechanics   ║ Performance-critical║
╚════════════════════╩════════════════════╩════════════════════╝
"""
print(comparison)