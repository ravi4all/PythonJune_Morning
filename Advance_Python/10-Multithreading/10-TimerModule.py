import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format=('[%(levelname)s] (%(threadName)-9s) %(message)s'))

def delayed():
    logging.debug("Starting")
    logging.debug("Exiting")

t1 = threading.Timer(3, delayed)
t1.setName("Thread-1")

t2 = threading.Timer(5, delayed)
t2.setName("Thread-2")

logging.debug("Starting Timers")
t1.start()
t2.start()

logging.debug("Waiting before cancellation of thread %s"%(t2.getName()))
time.sleep(2)
logging.debug("Cancelling %s"%(t2.getName()))
t2.cancel()