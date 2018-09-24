import multiprocessing
import time
from random import randint

CHECK_PERIOD_MS = 200
PRINT_PERIOS_MS = 2000

def worker(worker_id):
    # Sleep a random amount of time from 1 to 4s.
    time.sleep(randint(1,4))
    print(f'worker with id = {worker_id} finished.')

def map_async_test(num_tasks, check_period_ms, print_period_ms):
    """
    This will create `num_tasks` number of subprocesses, and report
    back on the completeion status of the processes every `print_period_ms`.
    """
    pool = multiprocessing.Pool(processes=4)
    rs = pool.map_async(worker, range(num_tasks))

    print_counter = 0
    while (True):
        if (rs.ready()): break
        remaining = rs._number_left
        if print_counter >= PRINT_PERIOS_MS/CHECK_PERIOD_MS:
            print("Waiting for", remaining, "tasks to complete...")
            print_counter = 0
        time.sleep(CHECK_PERIOD_MS/1000.0)
        print_counter += 1

    # result_worker_standard.wait()

def imap_unordered_test(num_tasks):
    pool = multiprocessing.Pool(processes=4)
    rs = pool.imap_unordered(worker, range(num_tasks))
    while (True):
        completed = rs._index
        if (completed == num_tasks): break
        print(f'Waiting for {num_tasks-completed} tasks to complete...')
        time.sleep(2)

if __name__ == '__main__':
    print('main() called.')
    
    map_async_test(10, CHECK_PERIOD_MS, PRINT_PERIOS_MS)
    # imap_unordered_test(10)

    print('main() finished.')
