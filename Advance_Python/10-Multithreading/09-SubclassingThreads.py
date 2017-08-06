import threading
import logging

logging.basicConfig(level=logging.DEBUG, format=('[%(levelname)s] (%(threadName)-9s) %(message)s'))


class MyThread(threading.Thread):

    def run(self):
        print("Run method is now overriden...")
        logging.debug("Running")


for i in range(5):
    t = MyThread()
    t.start()