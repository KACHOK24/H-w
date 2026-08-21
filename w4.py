# kvadrat = lambda x: x ** 2

# print(kvadrat(7))

# a = 50
# b = 23

# katta = lambda a, b: max(a, b)

# print(katta(a, b))


# sonlar = [2, 4, 6, 8, 10]

# natija = list(map(lambda x: x * 3, sonlar))

# print(natija)

# ismlar = ["ali", "vali", "sardor", "bobur"]

# natija = list(map(lambda x: x.upper(), ismlar))

# print(natija)


mahsulotlar = [
    ("Laptop", 800),
    ("Phone", 500),
    ("Mouse", 25),
    ("Keyboard", 70),
    ("Monitor", 300)
]


osish = sorted(mahsulotlar, key=lambda x: x[1])
print(osish)
kamayish = sorted(mahsulotlar, key=lambda x: x[1], reverse=True)
print(kamayish)
qimmat = list(filter(lambda x: x[1] > 100, mahsulotlar))
print(qimmat)