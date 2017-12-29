squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

squares2 = [i**2 for i in range(1, 101)]
print(squares2)

remainders5 = [x**2 % 5 for x in range(1, 101)]
print(remainders5)

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone with the Wind", "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Raiders of the Lost Ark", "Groundhog Day", "Close Encounters of the Third Kind"]

gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)

tmovies = [title for title in movies if title.startswith("T")]
print(tmovies)

movies = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946), ("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1954), ("The Lord of the Rings", 2001), ("Groundhog Day", 1993), ("Close Encounters of the Third Kind", 1977), ("The Royal Tenenbaums", 2001), ("The Aviator", 2004), ("Raiders of the Lost Arc", 1981)]

pre2k = [title for (title, year) in movies if year < 2000]

print(pre2k)

v = [2, -3, 1]

w = [4 * x for x in v]
print(w)

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]

print(cartesian_product)
