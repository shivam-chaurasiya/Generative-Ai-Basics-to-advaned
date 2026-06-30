item_price_inr = {
    "Burger": 80,
    "Pizza": 180,
    "Protein-Shake": 200
}

item_price_in_usd = {item: price/80 for item, price in item_price_inr.items()}
print(item_price_in_usd)

cubes = {x: x**3 for x in range(1, 4)}
print(cubes)
