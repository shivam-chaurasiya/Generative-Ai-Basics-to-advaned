squares = [1, 4, 9, 16, 25]
print(squares)

new_list = squares + [36, 49, 64, 81, 100]
print(new_list)

new_list.append(121)
print(new_list)

new_list.insert(0, 0)
print(new_list)

last_added = new_list.pop()
print(f'last removed {last_added}')

new_list.reverse()
print(f"reverse: {new_list}")

new_list.sort()
print(f"sort: {new_list}")
