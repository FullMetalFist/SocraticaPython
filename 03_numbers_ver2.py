# Types of numbers: int, long, float, complex
# Whole numbers: int, long

a = 28  # This is a perfect number
type(a)
a
print(a)

import sys
sys.maxint

b = 2147483647
type(b)

c = 2147483648
type(c)
print(c)


d = -sys.maxint - 1
type(d)
d

e = -2147483649

# Float
e = 2.718281828
type(e)

# Complex numbers
z = 3 +5.7j
type(z)
z.real
z.imag
