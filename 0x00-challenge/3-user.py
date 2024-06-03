#!/usr/bin/python3
"""
User class
"""

class User:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    def is_valid_password(self, password):
        return self.__password == password

if __name__ == "__main__":
    user = User("Test", "password")
    if not user.is_valid_password("password"):
        print("is_valid_password should return True if it's the right password")
    else:
        print("Test User")
