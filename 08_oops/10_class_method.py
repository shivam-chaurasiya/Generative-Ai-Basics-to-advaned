class PizzaOrder:
    def __init__(self, pizza_type, size):
        self.pizza_type = pizza_type
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["pizza_type"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        pizza_type, size = order_string.split("-")
        return cls(pizza_type, size)

class PizzaUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(PizzaUtils.is_valid_size("Medium"))

order1 = PizzaOrder.from_dict({"pizza_type": "Veggi", "size":"Large"})

order2 = PizzaOrder.from_string("Margerita-Small")

order3 = PizzaOrder("Large", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
    