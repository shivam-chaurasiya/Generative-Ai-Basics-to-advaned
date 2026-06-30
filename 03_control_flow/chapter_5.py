list = ["apple", "mango", "banana", "not fruit", "strawberry"]

for list in list:
    if list == "not fruit":
        continue
    if list == "strawberry":
        print(f"{list} box found")
        break
    print(f"{list} box found")

print(f"outside the loop")