import re

password = input()

isValid = True

if not 6 <= len(password) <= 10:
    print( "Password must be between 6 and 10 characters")
    isValid = False
if not password.isalnum():
    print("Password must consist only of letters and digits")
    isValid = False
if not re.search(".*\d.*\d", password):
    print("Password must have at least 2 digits")
    isValid = False

if isValid:
    print("Password is valid")

