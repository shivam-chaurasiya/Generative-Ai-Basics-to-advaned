class OutOfIngredientsError(Exception):
    pass

def make_milk_shake(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("Milk_Shake is ready...")

make_milk_shake(0,4)