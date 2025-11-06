row = 5
for i in range(1, row + 1):
    print("*" * i)

"""
for i in range(1, rows + 1):

The range(1, rows + 1) means → numbers 1 to 5 (1, 2, 3, 4, 5).

So the loop runs 5 times, once for each row.

At each iteration:

i takes values → 1, 2, 3, 4, 5
print("*" * i)

"*" is a string.

When you multiply a string by a number, it repeats that string.

"*" * 1 → "*"

"*" * 2 → "**"

"*" * 3 → "***"

and so on...

So each loop prints a row with i stars.
"""
