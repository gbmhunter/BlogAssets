import multiprocessing
import time

global lock

def init(l):
    global lock
    lock = l


def run_processes(worker):

    numbers = range(10)
    
    l = multiprocessing.Lock()
    pool = multiprocessing.Pool(initializer=init, initargs=(l,))
    pool.map(worker, numbers)
    pool.close()
    pool.join()
