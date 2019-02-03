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

import matplotlib.pyplot as plt
import numpy as np

import util

NUM_OBJECTS = 1000
# NUM_OBJECTS = 10000

def main():

    # Check if inputs already exist
    if os.path.isdir('test'):
        print('test directory already present, not generating input files.')
        return

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
        getattr(util, f'{serial_format}_write')(file_data)

if __name__ == '__main__':
    main()