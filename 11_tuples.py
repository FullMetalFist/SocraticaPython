# List example
prime_numbers = [2, 3, 5, 7]

# Tuple example
perfect_squares = (1, 4, 9, 16)

print("List methods")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods")
print(dir(perfect_squares))

import sys
print(dir(sys))
print(help(sys.getsizeof))

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2, 3, "a", "b", "c", True, 3.14159)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

# Lists are mutable, Tuples are immutable

import timeit

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("list time: ", list_test)
print("tuple time: ", tuple_test)

empty_tuple = ()
test1 = ("a",)           # if we don't include the comma ',' it will become a String
test2 = ("a","b")
test3 = ("a","b","c")

print(empty_tuple)
print(test1)
print(test2)
print(test3)

# (age, country, knows_python)
survey = (27. "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2

print("Age = ", age)
print("Country = ", country)
print("Knows Python? ", knows_python)
