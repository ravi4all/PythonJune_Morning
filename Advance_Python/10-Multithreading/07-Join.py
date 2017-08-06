import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format=('[%(levelname)s] (%(threadName)-9s) %(message)s'))

def daemon():

    logging.debug("Starting")
    for i in range(10000000):
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

# 3 - Timeout
t1.join(8)