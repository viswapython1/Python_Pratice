# Function to calculate the square of a positive number
# def square_number():
#     num = float(input("Enter a positive number: "))
#     if num > 0:
#         result = num ** 2
#         print(f"The square of {num} is {result}")
#     else:
#         print("Please enter a positive number only!")
#
#
# # Function call
# square_number()
# -----------------------------------
def square(num):
    return num ** 2


number = float(input("Enter a positive number: "))
print("Square:", square(number))
