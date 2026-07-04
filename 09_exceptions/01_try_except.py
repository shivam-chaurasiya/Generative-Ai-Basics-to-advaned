Pizza = {"Margerita": 300, "Veggi": 200}

try:
    Pizza["Paneer"]
except KeyError:
    print("The key that you are trying to access does not exists")

print("Hello Pizza World")

