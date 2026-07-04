class Pizza:
    type = "Veggi"
    Quantity = 4
    PricePerItem = 200

order = Pizza()
print(order.PricePerItem)

order.PricePerItem = 250
order.Quantity = 5
print("After changing", order.PricePerItem)
print("After changing", order.Quantity)
print("Direct look into the class", Pizza.PricePerItem)

del order.PricePerItem
del order.Quantity

print(order.PricePerItem)
print(order.Quantity)