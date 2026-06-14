basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

required_fruits = {'apple', 'banana', 'orange', 'litchi'}

print(f"basket contains {basket}")

all_fruits = basket | required_fruits
print(f"all fruits are {all_fruits}")

common_fruits = basket & required_fruits
print(f"common fruits are {common_fruits}")

only_in_basket = basket - required_fruits
print(f"fruits in basket {only_in_basket}")

#membership testing
print(f"Is apple in basket: {'apple' in basket}")