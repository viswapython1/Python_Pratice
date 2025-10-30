def triangle_type():
    # Taking inputs from the user
    side1 = int(input("Enter side 1: "))
    side2 = int(input("Enter side 2: "))
    side3 = int(input("Enter side 3: "))

    # Check type of triangle
    if side1 == side2 == side3:
        result = "eq"  # Equilateral
    elif side1 == side2 or side2 == side3 or side1 == side3:
        result = "iso"  # Isosceles
    else:
        result = "sca"  # Scalene

    return result


# Function call
triangle_result = triangle_type()
print("Triangle type is:", triangle_result)
