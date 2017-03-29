# for cryptographically secure pseudo-random number generator
# use os.urandom() or SystemRandom

import random
print(dir(random))

print(help(random.random))

# Display 10 random numbers from interval [0, 1)

for i in range(10):
    print(random.random())

# generate random numbers from interval [3, 7)

def my_random():
    # random, scale, shift, return...
    return 4*random.random() + 3

for i in range(10):
    print(my_random())

help(random.uniform)

for i in range(10):
    print(random.uniform(3, 7))

for i in range(20):
    print(random.randint(1, 6))

outcomes = ['rock', 'paper', 'scissors']

for i in range(20):
    print(random.choice(outcomes))
