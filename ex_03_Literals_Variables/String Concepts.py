
#🧠 What is a String in Python?

#A string is a sequence of characters enclosed in single (' '), double (" "), or triple quotes (''' ''' / """ """).
str1 = 'Hello'
str2 = "World"
str3 = '''This is 
a multiline string'''
print(str1,"\n",str2,"\n",str3)
print("\n")

"""
🧱 2️⃣ String Indexing and Slicing
Python strings are indexed — the first character starts at 0."""
s = "PYTHON"
print(s[0])     # P
print(s[-1])    # N (negative index)
print(s[1:4])   # YTH
print(s[:3])    # PYT
print(s[3:])    # HON
print(s[::-1])  # Reverses string → NOHTYP

#🔁 3️⃣ String Concatenation and Repetition
a = "Hello"
b = "World"

print(a + " " + b)  # Hello World
print(a * 3)        # HelloHelloHello

"""
📏 4️⃣ String Functions / Methods

Here’s a list of the most useful string built-in methods 👇
| Method          | Description                         | Example                              |
| --------------- | ----------------------------------- | ------------------------------------ |
| `len(s)`        | Returns length of string            | `len("Hi") → 2`                      |
| `upper()`       | Converts to uppercase               | `"hi".upper() → 'HI'`                |
| `lower()`       | Converts to lowercase               | `"Hi".lower() → 'hi'`                |
| `title()`       | Capitalizes each word               | `"hello world".title()`              |
| `capitalize()`  | Capitalizes first letter            | `"hello".capitalize()`               |
| `swapcase()`    | Swaps case                          | `"HeLLo".swapcase()`                 |
| `strip()`       | Removes leading/trailing spaces     | `"  hi  ".strip()`                   |
| `lstrip()`      | Removes left spaces                 | `"  hi".lstrip()`                    |
| `rstrip()`      | Removes right spaces                | `"hi  ".rstrip()`                    |
| `replace(a, b)` | Replace substring                   | `"bad".replace("b","g") → 'gad'`     |
| `split()`       | Splits string into list             | `"a,b,c".split(",") → ['a','b','c']` |
| `join()`        | Joins elements into string          | `" ".join(['hi','bye']) → 'hi bye'`  |
| `find()`        | Finds index of substring            | `"hello".find("e") → 1`              |
| `index()`       | Same as find but error if not found | `"hello".index("l") → 2`             |
| `count()`       | Counts occurrences                  | `"banana".count("a") → 3`            |
| `startswith()`  | Checks if starts with substring     | `"hello".startswith("he")`           |
| `endswith()`    | Checks if ends with substring       | `"world".endswith("ld")`             |
| `isalpha()`     | True if all letters                 | `"abc".isalpha()`                    |
| `isdigit()`     | True if all digits                  | `"123".isdigit()`                    |
| `isalnum()`     | True if letters + numbers           | `"abc123".isalnum()`                 |
| `isspace()`     | True if only spaces                 | `"   ".isspace()`                    |
| `isupper()`     | True if all uppercase               | `"HELLO".isupper()`                  |
| `islower()`     | True if all lowercase               | `"hello".islower()`                  |


"""

#🧮 5️⃣ String Formatting

#Used to insert variables inside strings dynamically.

#✅ Using format()

name = "Viswa"
age = 22
print("My name is {} and I am {} years old".format(name, age))
print("My name is {1} and I am {0}".format(age, name))

#Using % formatting
name = "Viswa"
age = 22
print("My name is %s and I am %d years old." % (name, age))

#String Comparison
a = "apple"
b = "banana"
print(a == b)   # False
print(a < b)    # True (lexicographically)

# String Iteration
#You can loop through a string easily:

for ch in "Hello":
    print(ch)

#💡String Immutability
#Strings in Python are immutable, meaning you can’t change them directly:

s = "Python"
# s[0] = 'J' ❌ (Error)
s = "J" + s[1:]  # ✅ Creates new string
print(s)

"""
🧩 9️⃣ Escape Characters
Used to include special characters in strings.
Escape	Meaning
\'	Single quote
\"	Double quote
\\	Backslash
\n	New line
\t	Tab
\r	Carriage return
"""

print("Hello\nWorld")
print("This is a tab:\tPython")

# String full example
s = "  Hello Python  "
print("Original:", s)
print("Length:", len(s))
print("Trimmed:", s.strip())
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Title:", s.title())
print("Count of 'l':", s.count('l'))
print("Find 'Python':", s.find('Python'))
print("Replace:", s.replace("Python", "World"))
print("Reversed:", s[::-1])
print("Split:", s.split())
print("Joined:", '-'.join(s.split()))
print(f"Formatted: Hello, length of string is {len(s)}")
