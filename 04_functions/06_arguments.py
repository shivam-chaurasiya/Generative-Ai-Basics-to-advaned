def vehicle(type, fuel, price):
    print(type,fuel,price)

vehicle("Car", "Diesel", 200000) #positinal
vehicle(type="bike", price=30000, fuel="petrol") #keyword

def special_pizza(*ingredients, **extras):
    print("ingredients", ingredients)
    print("extras", extras)

special_pizza("cheese", "onion", "chilli", size="medium", other_ingredients = ["chilli-flakes, oregano,tomato-sause"])