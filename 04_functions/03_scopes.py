def serve_pizza():
    pizza_size = "Small" # local scope
    print(f"Serve pizza of {pizza_size} size")

pizza_size = "Medium"
serve_pizza()
print(f"Outside the function: {pizza_size}")


def serve_burger():
    burger_type = "Veggi" # Enclosing Scope
    def serve_order():
        burger_type = "Paneer"
        print(f"Serve order at table 2: {burger_type}")
    serve_order()
    print("Outer:", burger_type)

burger_type = "Chesse Burger"
serve_burger()
print("Global:", burger_type)

