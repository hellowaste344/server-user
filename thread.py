import threading
import time


def task1():
    threading.Lock()
    print("Running Task1...")
    time.sleep(1)


def task2():
    print("Running Task2...")
    time.sleep(1)


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
t1.join()
t2.join()

print("\nThreads Completed\n")
