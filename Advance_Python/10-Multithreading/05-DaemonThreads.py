# Daemon Vs Non-Daemon Thread

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format=('[%(levelname)s] (%(threadName)-9s) %(message)s'))

def daemon():
    logging.debug("Starting")
    time.sleep(5)
    for x in range(100000):
        print(x)
    print("Completed Iterations...",x)
    logging.debug("Exiting")

thread_1 = threading.Thread(target=daemon, name='Daemon')
thread_1.setDaemon(True)

def non_daemon():
    logging.debug("Starting")
    time.sleep(3)
    logging.debug("Exiting")


thread_2 = threading.Thread(target=non_daemon, name="Non-Daemon")

thread_1.start()
thread_2.start()