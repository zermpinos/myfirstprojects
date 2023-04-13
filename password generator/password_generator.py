"""
password_generator.py
This program a random password of n digits, where n is given by the user, that also features error-handling.

Usage:
    python password_generator.py

Requirements:
    - Python 3.x
    - random module
    - string module

Parameters:
    - password_length: The length of the password.
        Its value is given by the user.
    - password: The password it self.

Functions:
    - generate_password(length):
        This function takes length as input and generates a password of letters, digits and symbols.

Author:
    Panagiotis Zermpinos

Version:
    1.0 (April 2023)
"""

import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


password = None
while True:
    try:
        password_length = int(input("Enter the length of your password: "))
        if password_length <= 0:
            print("Length must be a positive integer. Please try again.")
            continue
        password = generate_password(password_length)
        break
    except ValueError:
        print("Length must be an integer. Please try again.")

if password is not None:
    print(f"Your random password is: {password}")
else:
    print("No password was generated due to an error.")
# Wait for user input before exiting
input("Press any key to exit...")
