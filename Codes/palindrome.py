"""You are a Python developer. Implement a function palindrome using conditional logic and loops.
Rules:
ignore case,spaces and punctuation
handle edge cases  as empty string and single character
Write doctest test cases inside the function’s docstring
Add code at the end to run doctest using doctest.testmod()."""
def palindrome(s):
    """
    Check if the input string is a palindrome.
    >>> palindrome("A man, a plan, a canal, Panama")            
    True
    >>> palindrome("Hello, World!")
    False
    >>> palindrome("")
    True
    >>> palindrome("a")
    True    
    >>> palindrome("No 'x' in Nixon")
    True
    """
    # Remove spaces and punctuation, and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    