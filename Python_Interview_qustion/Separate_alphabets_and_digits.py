s = input("enter the string: ")
print(s)

alphabets = ""
digits = ""

for ch in s:
    if ch.isalpha():  # checks if the character is a letter
        alphabets += ch
    elif ch.isdigit():  # checks if the character is a number
        digits += ch

print("Alphabets:", alphabets)
print("Digits:", digits)
