
"""
Basic / Utility Functions
| Function    | Description                                |
| ----------- | ------------------------------------------ |
| `print()`   | Displays output to the console             |
| `type()`    | Returns the type of an object              |
| `id()`      | Returns the unique identifier of an object |
| `help()`    | Displays documentation about an object     |
| `dir()`     | Lists valid attributes of an object        |
| `len()`     | Returns the length of an object            |
| `input()`   | Takes user input                           |
| `eval()`    | Evaluates a string as Python code          |
| `exec()`    | Executes dynamically created Python code   |
| `globals()` | Returns a dictionary of global variables   |
| `locals()`  | Returns a dictionary of local variables    |
| `vars()`    | Returns `__dict__` attribute of an object  |

Numeric Functions
| Function       | Description                             |
| -------------- | --------------------------------------- |
| `abs()`        | Returns absolute value                  |
| `round()`      | Rounds a number                         |
| `pow(x, y)`    | Returns `x` to the power of `y`         |
| `sum()`        | Returns sum of all items in an iterable |
| `min()`        | Returns smallest item                   |
| `max()`        | Returns largest item                    |
| `divmod(a, b)` | Returns `(a // b, a % b)` as a tuple    |


Type Conversion Functions
| Function       | Description                      |
| -------------- | -------------------------------- |
| `int()`        | Converts to integer              |
| `float()`      | Converts to float                |
| `complex()`    | Creates a complex number         |
| `bool()`       | Converts to boolean              |
| `str()`        | Converts to string               |
| `list()`       | Converts to list                 |
| `tuple()`      | Converts to tuple                |
| `set()`        | Converts to set                  |
| `dict()`       | Creates a dictionary             |
| `frozenset()`  | Creates an immutable set         |
| `bytes()`      | Converts to bytes                |
| `bytearray()`  | Mutable version of bytes         |
| `memoryview()` | Returns memory view of an object |
| `bin()`        | Converts to binary string        |
| `oct()`        | Converts to octal string         |
| `hex()`        | Converts to hexadecimal string   |

🔁 Iterable / Sequence Functions
| Function      | Description                                 |
| ------------- | ------------------------------------------- |
| `range()`     | Generates a sequence of numbers             |
| `enumerate()` | Returns index and value from an iterable    |
| `zip()`       | Combines two or more iterables element-wise |
| `map()`       | Applies a function to all items in iterable |
| `filter()`    | Filters items using a function              |
| `sorted()`    | Returns sorted list                         |
| `reversed()`  | Returns reversed iterator                   |
| `any()`       | Returns `True` if any element is true       |
| `all()`       | Returns `True` if all elements are true     |

📚 Object and Class Functions
| Function                     | Description                             |
| ---------------------------- | --------------------------------------- |
| `isinstance(obj, type)`      | Checks if object is instance of a class |
| `issubclass(cls, classinfo)` | Checks if class is subclass of another  |
| `hasattr(obj, name)`         | Checks if object has an attribute       |
| `getattr(obj, name)`         | Gets attribute value                    |
| `setattr(obj, name, value)`  | Sets attribute value                    |
| `delattr(obj, name)`         | Deletes attribute                       |
| `callable()`                 | Checks if object is callable            |
| `super()`                    | Calls parent class method               |
| `staticmethod()`             | Defines a static method                 |
| `classmethod()`              | Defines a class method                  |
| `property()`                 | Creates managed attributes              |


📄 Input/Output and File Functions
| Function   | Description                                                 |
| ---------- | ----------------------------------------------------------- |
| `open()`   | Opens a file and returns a file object                      |
| `format()` | Formats a value                                             |
| `repr()`   | Returns a string representation of an object                |
| `ascii()`  | Returns a readable version of an object (escapes non-ASCII) |

⚙️ Miscellaneous / Advanced
| Function       | Description                         |
| -------------- | ----------------------------------- |
| `__import__()` | Imports a module programmatically   |
| `hash()`       | Returns hash value of an object     |
| `memoryview()` | Returns memory view object          |
| `object()`     | Creates a new base object           |
| `slice()`      | Creates a slice object              |
| `compile()`    | Compiles source code to code object |
| `chr()`        | Returns character from Unicode code |
| `ord()`        | Returns Unicode code from character |



"""

# Python program using many built-in functions
numbers = [1, 2, 3, 4, 5]

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Binary of 10:", bin(10))
print("All > 0:", all(n > 0 for n in numbers))
print("Any > 4:", any(n > 4 for n in numbers))
print("Enumerate:", list(enumerate(numbers)))
print("Zip:", list(zip(numbers, ['a', 'b', 'c', 'd', 'e'])))
print("Sorted (desc):", sorted(numbers, reverse=True))
