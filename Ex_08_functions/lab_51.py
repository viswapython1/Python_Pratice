"""
Python Functions are a block of statements that does a specific task.
 The idea is to put some commonly or repeatedly done task together and make a function
  so that instead of writing the same code again and again for different inputs,
   we can do the function calls to reuse code contained in it over and over again.
"""

# def fun():
#     print("welcome to GFG")
#
#
# fun()
"""
Function Arguments
Arguments are the values passed inside the parenthesis of the function.
 A function can have any number of arguments separated by a comma.
Syntax:
def function_name(parameters):
    #Docstring
    # body of the function
    return expression
"""

# def Check_even_or_odd(num):
#     if (num % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")
#
#
# num = int(input("Enter a number: "))
# Check_even_or_odd(num)

"""
2. Keyword Arguments
In keyword arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.
"""


# def student(fname, lname):
#     print(fname, lname)
#
#
# student(fname='Geeks', lname='Practice')
# student(lname='Practice', fname='Geeks')


def student_info(*args, **kwargs):
    print("Subjects:", args)  # Positional arguments
    print("Details:", kwargs)  # Keyword arguments


# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English", Name="Alice", Age=20, City="New York")
