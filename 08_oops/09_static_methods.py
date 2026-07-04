class PizzaUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = "cheese, veggies, ovan, oregano, etc"

cleaned = PizzaUtils.clean_ingredients
print(cleaned)

