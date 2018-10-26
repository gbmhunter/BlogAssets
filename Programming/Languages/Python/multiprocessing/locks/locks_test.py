import locks 
import time

def worker(args):
    number = args
    # lock = lockable.get_lock()
    locks.lock.acquire()
    print(f'number = {number}')
    time.sleep(1)
    print(f'number = {number}')
    locks.lock.release()

locks.run_processes(worker)