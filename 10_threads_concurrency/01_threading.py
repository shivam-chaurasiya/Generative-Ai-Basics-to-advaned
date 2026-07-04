import threading
import time

def take_orders():
    for i in range (1, 4):
        print(f"taking order for #{i}")
        time.sleep(2)

def make_pizza():
    for i in range(1, 4):
        print(f"Making pizza for #{i}")
        time.sleep(3)

#create threads

order_thread = threading.Thread(target=take_orders)
make_thread = threading.Thread(target=make_pizza)

order_thread.start()
make_thread.start()

#wait for both to finish

order_thread.join()
make_thread.join()

print(f"All orders taken and pizza made")