import threading
# import _thread

def worker(num):
    # print("Thread Running...",num)
    for i in range(0,100000):
        pass
    print(i)

threads = []

def print_me():
    print("Hello.......")

for t in range(5):
    obj = threading.Thread(target=worker, args=(t,))
    threads.append(obj)
    obj.start()
    print_me()
    print(obj.getName())
    print(obj.isAlive())