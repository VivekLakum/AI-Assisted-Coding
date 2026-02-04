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
