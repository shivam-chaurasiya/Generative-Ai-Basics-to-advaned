class BasePizza:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"preparing {self.type}  pizza...")

class MargeritaPizza(BasePizza):
    def add_items(self):
        print("Adding more cheese,Onion etc..")

class PizzaShop:
    pizza_cls = BasePizza   #composition

    def __init__(self):
        self.pizza = self.pizza_cls("Veggi")

    def serve(self):
        print(f"Serving {self.pizza.type} pizza")
        self.pizza.prepare()

class FancyPizzaShop(PizzaShop):
    pizza_cls = PizzaShop


shop = PizzaShop()
fancy = FancyPizzaShop()

shop.serve()
fancy.serve()
fancy.chai.add_items()