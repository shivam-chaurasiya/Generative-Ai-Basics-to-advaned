class Pizza:
    def __init__(self, type_, price):
        self.type = type_
        self.price = price

# class MargeretaPizza(Pizza):
#     def __init__(self, type_, price, isExtreCheese):
#         self.type = type_
#         self.price = price
#         self.isExtraCheese = isExtreCheese

# class MargeritaPizza(Pizza):
#     def __init__(self, type_, price,isExtreCheese):
#         Pizza.__init__(self, type_, isExtreCheese)
#         self.isExtraCheese = isExtreCheese

class MargeritaPizza(Pizza):
    def __init__(self, type_, price, isExtraCheese):
        super().__init__(type_, price)
        self.isExtraCheese = isExtraCheese