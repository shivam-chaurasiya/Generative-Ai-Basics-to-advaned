vowels = {char for char in "programming" if char in "aeiou"}

print(vowels)

favourite_dishes = [
    "Pizza", "Samosa", "Burger", 
    "Protein-Shake", "Green tea" 
]

unique_dish = {dish for dish in favourite_dishes if len(dish) < 9}
print(unique_dish)

items = {
    "Fast-Food":["Burger", "Pizza", "Samosa"],
    "Healthy-Food": ["Salad", "Green-tea","Protein-Shake"],
    "Non-Veg-Food": ["Fish", "Chicken", "Eggs"]
}

unique_item = {item for food in items.values() for item in food}

print(unique_item)