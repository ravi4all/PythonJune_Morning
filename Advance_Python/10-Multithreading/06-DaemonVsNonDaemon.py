import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format=('[%(levelname)s] (%(threadName)-9s) %(message)s'))


# def worker(num):
#
#     logging.debug("Starting")
#     time.sleep(5)
#     logging.debug("Exiting")
#
#
# for i in range(5):
#     obj = threading.Thread(target=worker, args=(i,))
#     obj.start()

def daemon():

    logging.debug("Starting")
    for i in range(100000000):
        pass
    print("Completed Iterations..",i)
    logging.debug("Exiting")

t1 = threading.Thread(target=daemon, name="Daemon")
t1.setDaemon(True)


def non_daemon():

    logging.debug("Starting")
    time.sleep(3)
    logging.debug("Exiting")

t2 = threading.Thread(target=non_daemon, name="Non-Daemon")

t1.start()
t2.start()