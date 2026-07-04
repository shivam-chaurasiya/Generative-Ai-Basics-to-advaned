import threading
import time

def prepare_pizza(type_, wait_time):
    print(f"{type_} pizza: preparing")
    time.sleep(wait_time)
    print(f"{type_} pizza: ready to serve")

t1 = threading.Thread(target= prepare_pizza, args=("Veggi", 2))
t2 = threading.Thread(target= prepare_pizza, args=("Magerita", 4))

t1.start()
t2.start()
t1.join()
t2.join()