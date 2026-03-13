# """ Assume you are a developer who is working on a function to test a function called is_valid_username(username).your task is to implement it by using Test-Driven Development principles 
# It must follow these requirements:
# username len must be between 5 and 15 characters 
# must contain only alphabets and digits 
# must start with  an alphabet and at  last no spaces allowed
# Example  :
# assert is_valid_username("user123")==True 
# assert is_valid_username("123user")==False"""
# def is_valid_username(username):
#     if len(username) < 5 or len(username) > 15:
#         return False
#     if not username[0].isalpha():
#         return False
#     if not username.isalnum():
#         return False
#     if ' ' in username:
#         return False
#     return True
# # Test cases
# assert is_valid_username("user123") == True
# assert is_valid_username("123user") == False
# assert is_valid_username("user name") == False
# assert is_valid_username("user") == False
# assert is_valid_username("user1234567890123") == False
# assert is_valid_username("user_123") == False
# assert is_valid_username("User123") == True
# assert is_valid_username("user123 ") == False
# assert is_valid_username(" user123") == False
# assert is_valid_username("user123!") == False
# print("All test cases passed!")

""" Assume you are a developer who is working  
"""