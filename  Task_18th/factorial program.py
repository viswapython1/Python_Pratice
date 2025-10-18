# import math
#
# num = int(input("Enter a number: "))
#
# if num < 0:
#     print("❌ Factorial not defined for negative numbers.")
# else:
#     print(f"✅ Factorial of {num} is: {math.factorial(num)}")


# 2 nd way
# def factorial_iter(n):
#     if n < 0:
#         raise ValueError("Factorial not defined for negative numbers")
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#         print(f"Step {i - 1}: result = {result}")
#     return result
#
#
# try:
#     num = int(input("Enter a non-negative integer: "))
#     print(f"Factorial of {num} is: {factorial_iter(num)}")
# except ValueError as e:
#     print("Invalid input:", e)


# Simple factorial program
num = int(input("Enter a non-negative integer: "))

factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is:", factorial)
