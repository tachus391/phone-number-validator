'''You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.'''


import re
print("please input the number")
pattern = r"^[0][0-9]{10}$"
if re.match(pattern, input()):
    print("Valid")
else:
    print("Invalid")
