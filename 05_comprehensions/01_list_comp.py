menu = [
    "Veggi Burger",
    "Paneer Burger",
    "Chillii potato",
    "Onion Pizza"
    "Ginger Chai"
]

order = [my_order for my_order in menu if "Burger" in my_order]

print(order)

squares = [x**2 for x in range(5)]
print(squares)