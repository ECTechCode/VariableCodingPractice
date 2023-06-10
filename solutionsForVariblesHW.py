#Solution for the variableNamingAndOutputHW.py

# Variable assignments
my_var1 = 10  # Valid variable name
My_Var1 = 20  # Valid variable name (case-sensitive)
my_Var2 = 30  # Valid variable name
My_var2 = 40  # Valid variable name (case-sensitive)
var2 = 20  # Invalid: starts with a number; Corrected: var2

# Output predictions
print(my_var1)  # Output: 10
print(My_Var1)  # Output: 20
print(my_Var2)  # Output: 30
print(My_var2)  # Output: 40
# print(2nd_var)  # Invalid: starts with a number


#Solution for the variableConstants.py

# Constants declaration
STATETAX = 0.1235  # Valid constant name, but not following recommended convention (hard to read)
STATE_TAX = 0.1235  # Valid constant name, following recommended convention

# Incorrect reassignment
# STATETAX = 0.15  # Incorrect: Constants are meant to remain unchanged; Commented out to prevent incorrect reassignment

# Output predictions
print(STATETAX)  # Output: 0.1235
print(STATE_TAX)  # Output: 0.1235

#Solution for textToComments.py

# This line is a comment

# Convert the following lines into comments

# Single-line comments
# print("Hello, World!")
# print("This is a Python program.")
# print("Comments are used to provide explanations.")

"""
Multi-line comments

print("Hello, World!")
print("This is a Python program.")
print("Comments are used to provide explanations.")
"""





