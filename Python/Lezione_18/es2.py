# Password Validation 1:  Write a function validate_password(password) that checks whether a password meets the following criteria: Minimum length of 20 characters, At least three uppercase letters, At least four special characters (non-alphanumeric). If the password is valid, the function should return True. If the password is invalid, the function should raise a built-in exception (e.g., ValueError) with a message indicating which criteria were not met.

import re

def validate_password(password):
    if len(password) < 20:
        raise ValueError("ERROR: your password must be at least 20 characters long")
    
    uppercase_letters_count = len([character for character in password if character.isupper()])
    if uppercase_letters_count < 3:
        raise ValueError("ERROR: your password must have at least 3 uppercase letters")
    
    special_characters_count = len(re.findall(r'[^a-zA-Z0-9]', password))
    if special_characters_count < 4:
        raise ValueError("ERROR: your password must have at least 4 special characters")
    
    return True

try:
    password = "ENTER PASSWORD HERE"
    if validate_password(password):
        print("Your password is valid")
except ValueError as exception:
    print(f"ERROR: your password is invalid {exception}")
