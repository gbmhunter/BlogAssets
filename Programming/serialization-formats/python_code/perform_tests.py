#!/usr/bin/env python3

import random
import string
import sys
import timeit

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

import util

NUM_OBJECTS = 1000
# NUM_OBJECTS = 10000

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
        'toml',
        'yaml',
        'xml',
    ]

    timing_results_read = []

    print(f'Performing reads...')
    data = []
    for serial_format in serial_formats:
        print(f'Reading {serial_format}')
        read_func = getattr(util, f'{serial_format}_read')
        ret_val = measure_time(read_func)
        print(ret_val)
        timing_results_read.append(ret_val[0])
        data.append(ret_val[1])

    print(f'Performing writes...')
    timing_results_write = []
    for i, serial_format in enumerate(serial_formats):
        write_func = getattr(util, f'{serial_format}_write')
        print(f'Calling {write_func}...')
        ret_val = measure_time(write_func, data[i])
        timing_results_write.append(ret_val[0])



    print(f'timing_results_write = {timing_results_write}')
    print(f'timing_results_read = {timing_results_read}')

    ####################################################################################################
    # DRAW GRAPHS
    ####################################################################################################

    bar_width = 0.35
    x_positions = np.arange(0, len(serial_formats))
    fig, ax = plt.subplots()

    print(x_positions)
    print(timing_results_write)
    ax.bar(x_positions, timing_results_write, width=bar_width)
    ax.bar(x_positions + bar_width, timing_results_read, width=bar_width)

    ax.set_xlabel('Serialization Format')
    ax.set_xticks(x_positions)
    ax.set_xticklabels(serial_formats)

    ax.set_ylabel('Seconds (s)')

    ax.set_title('File Write/Read Times For Popular Serialization Formats')

    plt.savefig('test.png')


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
