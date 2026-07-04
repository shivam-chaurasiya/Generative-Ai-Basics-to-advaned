from multiprocessing import Process
import time

def make_Pizza(name):
    print(f"Start of {name} pizza making")
    time.sleep(3)
    print(f"End of {name} pizza making")

if __name__ == "__main__":
    pizza_makers = [
        Process(target=make_Pizza, args=(f"Pizza Maker #{i+1}",))
        for i in range(3)
    ]

    #start all process

    for p in pizza_makers:
        p.start()

    #wait for all to complete
    for p in pizza_makers:
        p.join()

    print("All pizza served")
