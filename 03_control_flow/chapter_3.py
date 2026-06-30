words = ["list", "union", "random", "range"]

for w in words:
    print(w, len(w))

# Enumerate with for loop 

for index, item in enumerate(words, start=1):
    print(f"{index}: {item}")

#Zip function

name = ["Shivam", "Gunjan","Sam", "Vishal"]
Bills = [90, 80, 100, 120]

for name, amount in zip(name, Bills):
    print(f"{name} paid  {amount}Rs bill")

for token in range(1, 5):
    print(f"Serving chai to token #{token}")