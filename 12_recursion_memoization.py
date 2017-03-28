# Fibonacci Sequence
# 0,1,1,2,3,5,8,13,21

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11):
    print(n, ":", fibonacci(n))


# Cache values
fibonacci_cache = {}

def fibonacci2(n):
    # if we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci2(n-1) + fibonacci2(n-2)

    # cache the value and return it
    fibonacci_cache[n] = value
    return value

# warning! the next loop is slow without caching
for n in range(1, 101):
    print(n, ":", fibonacci2(n))

for n in range(1, 1001):
    print(n, ":", fibonacci2(n))


from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci3(n):
    # check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
