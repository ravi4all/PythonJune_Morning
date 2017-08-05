import threading
import time

def worker(num):
    print("Thread {} sleeps for 5 seconds".format(num))
    print("Worker",num)
    time.sleep(5)
    print("Thread {} Woke Up".format(num))

threads = []

for i in range(5):
    obj = threading.Thread(target=worker, args=(i,))
    obj.start()