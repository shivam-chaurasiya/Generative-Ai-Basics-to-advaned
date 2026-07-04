def serve_items():
    yield "Table 1: Serve Pizza"
    yield "Table 2: Serve Burger"
    yield "Table 3: Serve Shake"
    yield "Table 4: Serve Milk"

stall = serve_items()

# for item in stall:
#     print(item)

print(next(stall))
# print(next(stall))
# print(next(stall))
# print(next(stall))

