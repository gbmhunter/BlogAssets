#!/usr/bin/env python3

import csv
import json
import os
import random
import string
import sys
import timeit
import toml
import yaml
import xml.etree.cElementTree as ET

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np

import util

NUM_OBJECTS = 10
# NUM_OBJECTS = 10000


SCRIPT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

INPUT_DIR = os.path.join(SCRIPT_DIR, '../', 'temp', 'input_files')

def main():

    # Check if inputs already exist
    if not os.path.isfile(os.path.join(INPUT_DIR, 'data.csv')):
        print(f'Creating input files...')
    else:
        print('temp/input_files/data.csv file already present, not generating input files.')
        return

    # Make directory if it doesn't already exist
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)

    file_data = []
    for i in range(NUM_OBJECTS):
        file_data.append({
            'id': i,
            'name': util.string_generator(),
            'address': util.string_generator(size=20),
            'age': random.uniform(0.0, 100.0),
        })

    serial_formats = [
        'csv',
        'json',
        'toml',
        'yaml',
        'xml',
    ]

    for serial_format in serial_formats:
        getattr(util, f'{serial_format}_write')(file_data, os.path.join(INPUT_DIR, f'data.{serial_format}'))

if __name__ == '__main__':
    main()