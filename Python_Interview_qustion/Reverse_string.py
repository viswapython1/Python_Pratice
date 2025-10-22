# Reverse a string without using built-in functions
"""Let’s go through a few different ways to reverse
a string without using built-in functions like [::-1], reversed(), or .join()."""
"""How it works:
Each time the loop runs, it takes one character from s and adds
 it before the previous characters — effectively reversing the order."""

s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + s
print(rev)


# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]
#
#
# s = "Python"
# print("Reversed:", reverse_string(s))

def reverse(s):
    if len(s) == 0:  # If the string is empty, return it immediately.
        return s  # This stops the recursion from running forever.
    else:
        return reverse(s[1:]) + s[0]  # s[1:] means “string without the first character.”
        # s[0] means “the first character.”
    """You call the same function again on the smaller string (s[1:])
    and when it returns, you add back the first character at the end."""


s = input("Enter a string: ")
print("reversed : ", reverse(s))
# -------------------------------------
s = "Python"
rev = "".join([s[i] for i in range(len(s) - 1, -1, -1)])
print("Reversed:", rev)

Name = input("Enter a name: ")
rev = "".join([s[i] for i in range(len(s) - 1, -1, -1)])
print("Reversed:", rev)
# ----------------------------------
"""range(len(s)-1, -1, -1)
This creates a sequence of indexes in reverse order.
len(s)-1	start from index 5 (last character)
-1	stop just before index -1 (so stops at 0)
-1	step backwards (decrease by 1 each time)
range(5, -1, -1) → [5, 4, 3, 2, 1, 0]
"""

s = input("Enter a string: ")
alphabets = ""
num = ""
for ch in s:
    if ch.isalpha():
        alphabets += ch
    elif ch.isdigit():
        num += ch
print(alphabets)
print(num)
