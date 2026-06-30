def calculate_bill(no_of_items, price_per_item):
    return no_of_items * price_per_item

my_bill = calculate_bill(5, 25)
print(my_bill)

print(f"Order for table 2:", calculate_bill(3,80) )