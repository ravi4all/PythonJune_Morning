import threading
import time

def f1():
    print("Starting",threading.current_thread().getName())
    time.sleep(2)
    print("Exiting",threading.current_thread().getName())

def f2():
    print("Starting",threading.current_thread().getName())
    time.sleep(2)
    print("Exiting",threading.current_thread().getName())

def f3():
    print("Starting",threading.current_thread().getName())
    time.sleep(2)
    print("Exiting",threading.current_thread().getName())

t1 = threading.Thread(target=f1)
t2 = threading.Thread(target=f2)
t3 = threading.Thread(target=f3)

t1.start()
t2.start()
t3.start()

# for i in range(3):
#     th = threading.Thread(target=f1)
#     th.start()