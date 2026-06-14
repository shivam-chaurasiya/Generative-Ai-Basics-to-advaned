# with immutable objects

amount = 20
print(f"initial value : {amount}")

amount = 30
print(f"second initial value : {amount}")

print(f"ID of 20: {id(20)}")
print(f"ID of 30: {id(30)}")

#with mutable objects

fruits = set()
print(f"initial fruits id: {id(fruits)}")
print(f"initial fruits: {fruits}")

fruits.add("mango")
fruits.add("banana")
fruits.add("apple")

print(f"fruits id: {id(fruits)}")
print(f"fruits: {fruits}")
