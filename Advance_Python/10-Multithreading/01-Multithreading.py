import threading

# The __init__() of the Thread class looks like this:
#
# def __init__(self, group=None, target=None, name=None,
#              args=(), kwargs=None, *, daemon=None):

def worker(num):
    print("Worker",num)

threads = []

for i in range(5):
    obj = threading.Thread(target=worker, args=(i,))
    threads.append(obj)
    obj.start()

    print(obj.isAlive())