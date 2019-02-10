#!/usr/bin/env python3

import csv
import os
import random
import string
import sys
import time
# import timeit

import numpy as np

import util

# Number of times the measure_time() function will test the function.
# Minimum time returned.
NUM_RERUNS = 3

# This template is used so we can return values from the called function
# timeit.template = """
# def inner(_it, _timer{init}):
#     {setup}
#     _t0 = _timer()
#     for _i in _it:
#         retval = {stmt}
#     _t1 = _timer()
#     return _t1 - _t0, retval
# """

def main():
    print('============================')
    print('perform_tests.main() called.')

    serial_formats = util.get_serial_formats()
    read_dir = os.path.join('temp', 'input_files')
    write_dir = os.path.join('temp', 'output_py')
    stats_dir = os.path.join('temp', 'stats')

    timing_results_read = []

    print(f'Performing reads...')
    data = []
    for serial_format in serial_formats:
        read_func = getattr(util, f'{serial_format}_read')
        ret_val = measure_time_v2(read_func, os.path.join(read_dir, f'data.{serial_format}'))
        timing_results_read.append(ret_val[0])
        data.append(ret_val[1])

    print(f'Performing writes...')
    if not os.path.exists(write_dir):
        os.makedirs(write_dir)
    timing_results_write = []
    for i, serial_format in enumerate(serial_formats):
        write_func = getattr(util, f'{serial_format}_write')
        ret_val = measure_time_v2(write_func, data[i], os.path.join(write_dir, f'data.{serial_format}'))
        timing_results_write.append(ret_val[0])


    print(f'timing_results_write = {timing_results_write}')
    print(f'timing_results_read = {timing_results_read}')

    print(f'Writing results to file.')
    with open(os.path.join(stats_dir, 'python_stats.csv'), 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Format', 'Read (ms)', 'Write (ms)'])
        for i in range(len(serial_formats)):
            csv_writer.writerow([ serial_formats[i], timing_results_read[i], timing_results_write[i] ])

# def wrapper(func, *args, **kwargs):
#     def wrapped():
#         return func(*args, **kwargs)
#     return wrapped

# def measure_time(func, *arguments):
#     wrapped = wrapper(func, *arguments)
#     # We only want to include one run in the time info
#     return timeit.timeit(wrapped, number=1)

def measure_time_v2(func, *arguments):
    run_times_s = []
    ret_vals = []
    for i in range(NUM_RERUNS):
        start_time = time.perf_counter()
        ret_val = func(*arguments)
        end_time = time.perf_counter()
        ret_vals.append(ret_val)
        run_times_s.append(end_time - start_time)

    # Return minimum run time, and the return value from the first time the function
    # was run
    print(f'run_times_s = {run_times_s}')
    return (min(run_times_s), ret_vals[0])

if __name__ == '__main__':
    main()
