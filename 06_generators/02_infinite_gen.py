import itertools

def infinte_shake():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1
    
refill = infinte_shake()

for _ in range(3):
    print(next(refill))

#1. built-in
for num in itertools.count(start=10, step=5):
    if num > 25:
        break
    print(num)

# 2. Cycle through a list continuously
traffic_light = itertools.cycle(['Red', 'Green', 'Yellow'])
print(next(traffic_light))  
print(next(traffic_light))  
print(next(traffic_light))  
print(next(traffic_light))

