class InvalidBurgerError(Exception): pass

def bill(item, quantity):
    menu = {"Deluxe": 80, "Veggi": 50}
    try:
        if item not in menu:
            raise InvalidBurgerError("That burger is not in our menu")
        if not isinstance(quantity,int):
            raise TypeError("quantity must be integer")
        total = menu[item] * quantity
        print(f"Your total bill is {total}")
    except Exception as e:
        print("Error:", e )
    finally:
        print("Thank you for visiting burger king...")

# bill("Super", 20)
# bill("Deluxe", "two")
bill("Veggi",5)