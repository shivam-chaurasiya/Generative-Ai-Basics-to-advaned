def pizza_customer():
    print("Welcome ! What pizza would you like")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = pizza_customer()
next(stall) # start the generator

stall.send("Onion Pizza")
stall.send("Paneer Pizza")