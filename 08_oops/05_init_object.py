class pizza:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size
    
    def summary(self):
        return f"A {self.type} Pizza of {self.size} size give to the customer"
    
order = pizza("Margerita", "Medium")
print(order.summary())

order_2 = pizza("Veggi", "Large")
print(order_2.summary())



        