car_type = "Diesel"
def update_Car():
    car_type = "Petrol"
    def Car():
        nonlocal car_type
        car_type = "CNG"
    Car()
    print(f"Car type: {car_type}")

update_Car()