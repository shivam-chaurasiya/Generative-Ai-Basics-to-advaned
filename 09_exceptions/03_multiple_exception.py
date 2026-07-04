def process_order(item, quantity):
    try:
        price = {"Delux_Pizza": 300, "Veggi_Pizza": 200}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that pizza is not on menu")
    except TypeError:
        print("Quantity must be in number")

# process_order("Delux_Pizza", 3)
process_order("Veggi_Pizza", 5)
process_order("super", 5)
process_order("Veggi_Pizza", "two")