age = 65
age+1
print(age)

age = 65 # int
"""
This is multi comment
1. Author- Pramod Dutta
2. Information
3. Print the age of pramod
"""
print(age)

gst = 18.45
print(type(gst))

result = max(45, 65)
result_min = min(45, 65)
print(result)
print(result_min)

# Built In - Functions
# Pre defind given by the Python guys to you to use it.

# max()
# min()
# print()
print(pow(2,3))
b = abs(-10) # Return the absolute value of the argument.
print(b)
# Logic Building

# Step 1
# I/P -> num1,num2 -> int
# O/P -> sum, mul, div (Always ask from interviewer) , float

# Step 2 - Rought Logic

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print(num1 + num2)
print(num1 * num2)
print(num1 / num2)
print(num1 - num2)

# Escape Sequence
# \n -> new line
# \t -> tab
# \b -> backspace (1 char backspace)

print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\bWorld")