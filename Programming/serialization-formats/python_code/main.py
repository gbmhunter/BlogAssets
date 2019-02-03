#!/usr/bin/env python3

import random
import string
import sys
import timeit

import matplotlib.pyplot as plt
import numpy as np

NUM_OBJECTS = 1000
# NUM_OBJECTS = 10000

def main():
    file_data = []
    for i in range(NUM_OBJECTS):
        file_data.append({
            'id': i,
            'name': string_generator(),
            'address': string_generator(size=20),
            'age': random.uniform(0.0, 100.0),
        })

    serial_formats = [
        'csv',
        'json',
        'toml',
        'yaml',
        'xml',
    ]

    timing_results_write = []
    for serial_format in serial_formats:
        timing_results_write.append(measure_time(getattr(sys.modules[__name__], f'{serial_format}_write'), file_data))

    timing_results_read = []
    for serial_format in serial_formats:
        timing_results_read.append(measure_time(getattr(sys.modules[__name__], f'{serial_format}_read')))


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

    plt.show()


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
