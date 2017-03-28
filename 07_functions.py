# input parameters between the parentheses.
def f():
    pass

f()

def ping():
    return "Ping!"

ping()

x = ping()
print(x)

# volume of a sphere
# V = (4/3)πr^3

import math

def volume(r):
    """Returns the volume of a sphere with radius r."""
    v = (4.0 / 3.0) * math.pi * r ** 3
    return v

print(volume(3))

def triangle_area(b, h):
    """Returns the areaof a triangle with base b and height h. """
    return 0.5 * b * h

triangle_area(3, 6)

# cm to inch
# 2.54 => 1
# inch to foot
# 12 => 1

def cm(feet = 0, inches = 0):
    """Converts a length from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm
