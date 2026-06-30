daily_item_sales = [5,10,12,3,5,12,56]

total_items = sum(sale for sale in daily_item_sales if sale > 5)

print(total_items)

res = (num for num in range(10) if num % 2 == 0)
print(list(res))