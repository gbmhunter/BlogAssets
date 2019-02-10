import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

import util

SCRIPT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
STATS_DIR = os.path.join(SCRIPT_DIR, '..', 'temp', 'stats')
OUTPUT_PY_DIR = os.path.join(SCRIPT_DIR, '..', 'temp', 'output_py') 

def main():
    analyze_stats_file(os.path.join(STATS_DIR, 'cpp_stats.csv'), 'C++', 'cpp')
    analyze_stats_file(os.path.join(STATS_DIR, 'python_stats.csv'), 'Python', 'python')
    analyze_file_size()

def analyze_stats_file(file_path: str, language: str, file_suffix: str) -> None:

    serial_formats = []
    timing_results_read = []
    timing_results_write = []

    # Read in data
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue
            
            serial_formats.append(row[0])
            timing_results_read.append(float(row[1]))
            timing_results_write.append(float(row[2]))

    print(f'serial_formats = {serial_formats}')
    print(f'timing_results_read = {timing_results_read}')
    print(f'timing_results_write = {timing_results_write}')

    ####################################################################################################
    # DRAW GRAPHS
    ####################################################################################################

    print(f'Creating graphs...')

    bar_width = 0.35
    x_positions = np.arange(len(serial_formats))
    fig, ax = plt.subplots()

    ax.bar(x_positions, timing_results_write,
            align='center',
            width=bar_width,
            label="Write Time")
    ax.bar(x_positions + bar_width, timing_results_read,
            align='center',
            width=bar_width,
            label="Read Time")

    ax.set_xlabel('Serialization Format')
    ax.set_xticks(x_positions + bar_width/2)
    ax.set_xticklabels(serial_formats)

    ax.set_ylabel('Seconds (s)')

    ax.legend()

    ax.set_title(f'{language} Read/Write Times For Popular Serialization Formats')

    plt.savefig(os.path.join(STATS_DIR, 
            f'serialization-formats-read-write-times-{file_suffix}.png'))

def analyze_file_size():
    print('Analyzing file sizes...')

    serial_formats = util.get_serial_formats()

    file_sizes_mb = []
    for serial_format in serial_formats:
        file_path = os.path.join(OUTPUT_PY_DIR, f'data.{serial_format}')
        # Item 6 is the size in bytes
        file_size_bytes = os.stat(file_path)[6]
        file_sizes_mb.append(file_size_bytes/(1024.0*1024.0))

    print(f'file_sizes_mb = {file_sizes_mb}')

    x_positions = np.arange(len(file_sizes_mb))

    fig, ax = plt.subplots()
    ax.bar(x_positions, file_sizes_mb)

    ax.set_xlabel('Serialization Format')
    ax.set_xticks(x_positions)
    ax.set_xticklabels(serial_formats)
    ax.set_ylabel('File Size (MiB)')
    ax.set_title('File Sizes For Popular Serialization Formats')

    plt.savefig(os.path.join(STATS_DIR, f'serialization-formats-file-sizes.png'))

if __name__ == '__main__':
    main()