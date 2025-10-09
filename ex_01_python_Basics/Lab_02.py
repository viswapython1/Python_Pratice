# ===== Python Variables Demonstration =====
usage_ = """
Topics we’ll cover in one program

Variable declaration

Data types (int, float, string, bool, complex, list, tuple, set, dict)

Multiple assignments

Type casting

Constants (by convention)

Dynamic typing (changing variable type)

Global & local variables

Deleting variables (del)

f-string formatting

id() and type() usage

"""


# 1️⃣ Simple variable declarations
name = "Viswa"
age = 25
height = 5.9
is_student = True
complex_num = 2 + 3j

# 2️⃣ Multiple assignment
x, y, z = 10, 20.5, "Hello"

# 3️⃣ Constant (by naming convention — not enforced)
PI = 3.14159

# 4️⃣ Different Data Types
numbers_list = [1, 2, 3, 4]          # list
numbers_tuple = (5, 6, 7, 8)         # tuple
numbers_set = {9, 10, 11}            # set
student_dict = {"name": name, "age": age, "student": is_student}  # dict

# 5️⃣ Type Casting
age_str = str(age)
height_int = int(height)
sum_result = int(x + y)

# 6️⃣ Dynamic Typing (same variable, different type)
value = 100
value = "Now I'm a string"

# 7️⃣ Global & Local Variables
global_var = "I am global"

def show_variables():
    local_var = "I am local"
    print("\nInside function:")
    print("Local:", local_var)
    print("Global (accessed inside):", global_var)

show_variables()

# 8️⃣ Deleting a variable
temp_var = "Temporary"
del temp_var  # variable deleted

# 9️⃣ f-string Formatting
print(f"\nName: {name}, Age: {age}, Height: {height}")
print(f"Sum of x and y (int cast): {sum_result}")

# 🔟 id() and type()
print("\n--- Type & ID Information ---")
print(f"name -> {type(name)}, id = {id(name)}")
print(f"numbers_list -> {type(numbers_list)}, id = {id(numbers_list)}")
print(f"PI -> {type(PI)}, id = {id(PI)}")

# ✅ Final Summary
print("\nAll variables demonstration completed successfully!")
