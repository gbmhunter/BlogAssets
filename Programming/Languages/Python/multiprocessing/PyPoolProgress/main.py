import multiprocessing
import time
from random import randint

PRINT_PERIOS_S = 2.0

def worker(worker_id):
    # Sleep a random amount of time from 1 to 4s.
    time_to_sleep = randint(1,4)
    time.sleep(time_to_sleep)
    print(f'worker with id = {worker_id} finished.')

    # Return something so we can show how results are collected in parent process
    return worker_id

def map_async_test(num_tasks, print_period_s):
    """
    This will create `num_tasks` number of subprocesses, and report
    back on the completeion status of the processes every `print_period_ms`.
    """
    pool = multiprocessing.Pool(processes=4, maxtasksperchild=1)

    start_time = time.time()
    async_result = pool.map_async(worker, range(num_tasks))

    while True:
        # Accessing "internal" variable in Python stdlib! Not the best practise, but no public API exists for this.
        # Be warned it may change without warning with different versions of Python. However, this is a non-critical
        # call as it's only used for logging (rs.ready() is used to loop termination)
        # _number_left is the number of "chunks" remaining, which is not the same as the number of tasks!!!
        remaining = async_result._number_left
        elapsed_time = time.time() - start_time
        print(f'Waiting for child processes to complete. Function = {worker.__name__}(), chunks remaining = {remaining}, elapsed time = {time.strftime("%H:%M:%S", time.gmtime(elapsed_time))}.')

        # Wait until all child processes are complete, or it's time to print log message again
        async_result.wait(print_period_s)

        if async_result.ready():
            break
        
    print(f'Child processes complete. Function = {worker.__name__}(), total time = {time.strftime("%H:%M:%S", time.gmtime(elapsed_time))}.')

    # Not sure if this is needed (worker processes should already be complete), 
    # but let's terminate just in case!
    pool.terminate()

    # Subprocesses must be finished! Print results
    print(f'results = {async_result.get()}')

if __name__ == '__main__':
    print('main() called.')
    
    map_async_test(10, PRINT_PERIOS_S)

    print('main() finished.')
