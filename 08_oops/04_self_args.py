class Pizza:
    size = "Medium"

    def describe(self):
        return f"A {self.size} pizza is serve"
    
order = Pizza()
print(order.describe())
print(Pizza.describe(order)) # Pass the object manually otherwise it will give error

order_two = Pizza()
order_two.size = "Large"
print(Pizza.describe(order_two))