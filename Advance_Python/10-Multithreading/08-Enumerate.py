import threading
import logging
import random
import time

logging.basicConfig(level=logging.DEBUG, format=('[%(levelname)s] (%(threadName)-9s) %(message)s'))

def worker():
    t = threading.current_thread()
    # logging.debug("Starting")
    pause = random.randint(1,6)
    logging.debug("{} sleeping for {} seconds".format(t.getName(), pause))
    time.sleep(pause)
    logging.debug("Exiting")

for i in range(10):
    th = threading.Thread(target=worker)
    th.setDaemon(True)
    th.start()

main_thread = threading.current_thread()

for t in threading.enumerate():
    if t is main_thread:
        logging.debug("Current thread %s"%(t.getName()))
        continue
    logging.debug("Joining thread %s"%(t.getName()))
    t.join()