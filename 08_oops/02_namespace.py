class Burger:
    origin = "India"

print(Burger.origin)

Burger.is_Veggi = True
print(Burger.is_Veggi)

#Creating Object from class burger

items = Burger()

# print(f"1234 {items}")

print(f"Burger {items.origin}")
print(f"Burger {items.origin}")

items.is_Veggi = False

print("Class:", Burger.is_Veggi)
print(f"items {items.is_Veggi}")

items.price = 90

print(items.price)


