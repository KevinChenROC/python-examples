import threading
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-0s) %(message)s',)


def show(d):
    try:
        val = d.val
    except AttributeError:
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', val)


def worker(d):
    show(d)
    d.val = random.randint(1, 100)
    show(d)


d = threading.local()
show(d)
d.val = 999
show(d)

for i in range(2):
    t = threading.Thread(target=worker, args=(d,))
    t.start()
