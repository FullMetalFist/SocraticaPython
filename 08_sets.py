
example = set()
dir(example)

help(example.add)

example.add(42)
example.add(True)
example.add(3.14159)
example.add("Thorium")

print(example)

len(example)

help(example.remove)

example.remove(42)

help(example.discard)

example.discard(50)

example2 = set([28, True, 2.71828, "Iron"])

len(example2)
example2.clear()
len(example2)

# integers 1 - 10
odds = set([1, 3, 5, 7, 9])
even = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

odds.union(evens)
evens.union(odds)
# odds & evens remain unchanged

odds.intersection(primes)
primes.intersection(evens)

2 in primes
6 in odds

9 not in evens
