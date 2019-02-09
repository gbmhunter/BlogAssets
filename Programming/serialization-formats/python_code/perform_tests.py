#!/usr/bin/env python3

import csv
import os
import random
import string
import sys
import timeit

import numpy as np

import util

timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    for _i in _it:
        retval = {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""

def main():

    serial_formats = [
        'csv',
        'json',
        'protobuf',
        'toml',
        'yaml',
        'xml',
    ]
    read_dir = os.path.join('temp', 'input_files')
    write_dir = os.path.join('temp', 'output_py')
    stats_dir = os.path.join('temp', 'stats')

    timing_results_read = []

    print(f'Performing reads...')
    data = []
    for serial_format in serial_formats:
        read_func = getattr(util, f'{serial_format}_read')
        ret_val = measure_time(read_func, os.path.join(read_dir, f'data.{serial_format}'))
        timing_results_read.append(ret_val[0]*1000.0)
        data.append(ret_val[1])

    print(f'Performing writes...')
    if not os.path.exists(write_dir):
        os.makedirs(write_dir)
    timing_results_write = []
    for i, serial_format in enumerate(serial_formats):
        write_func = getattr(util, f'{serial_format}_write')
        ret_val = measure_time(write_func, data[i], os.path.join(write_dir, f'data.{serial_format}'))
        timing_results_write.append(ret_val[0]*1000.0)


    print(f'timing_results_write = {timing_results_write}')
    print(f'timing_results_read = {timing_results_read}')

    print(f'Writing results to file.')
    with open(os.path.join(stats_dir, 'python_stats.csv'), 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['Format', 'Read (ms)', 'Write (ms)'])
        for i in range(len(serial_formats)):
            csv_writer.writerow([ serial_formats[i], timing_results_read[i], timing_results_write[i] ])

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def measure_time(func, *arguments):
    wrapped = wrapper(func, *arguments)
    # We only want to include one run in the time info
    return timeit.timeit(wrapped, number=1)


if __name__ == '__main__':
    main()
