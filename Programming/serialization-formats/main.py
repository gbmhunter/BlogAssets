#!/usr/bin/env python3

import csv
import json
import random
import string
import sys
import timeit
import toml
import yaml
import xml.etree.cElementTree as ET

from dicttoxml import dicttoxml
import xmltodict

NUM_OBJECTS = 10000

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
        timing_results_read.append(measure_time(getattr(sys.modules[__name__], f'{serial_format}_read'), file_data))


    print(f'timing_results = {timing_results}')

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def measure_time(func, arguments):
    wrapped = wrapper(func, arguments)
    return timeit.timeit(wrapped, number=1)

def csv_write(file_data):
    print(f'Writing .csv file.')
    with open('data.csv', 'w') as file:
        csv_writer = csv.writer(file, delimiter=',')
        # Write header row
        csv_writer.writerow(file_data['people'][0].keys())
        for person in file_data['people']:
            csv_writer.writerow(person.values())

def csv_read():
    print(f'Reading .csv file.')
    data = []
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for person in csv_reader:
             data.append(person) 
    return data

def json_write(file_data):
    print(f'Writing .json file.')
    with open('data.json', 'w') as file:
        json.dump(file_data, file)

def json_read():
    print(f'Writing .json file.')
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data

def toml_write(file_data):
    print(f'Writing .toml file.')
    with open('data.toml', 'w') as file:
        toml.dump(file_data, file)

def toml_read():
    print(f'Reading .toml file.')
    with open('data.toml', 'r') as file:
        data = toml.load(file)
    return data

def yaml_write(file_data):
    print(f'Writing .yaml file.')
    with open('data.yaml', 'w') as file:
        yaml.dump(file_data, file)

def yaml_read():
    print(f'Reading .yaml file.')
    with open('data.yaml', 'r') as file:
        data = yaml.load(file)
    return data

def xml_write(file_data):
    print(f'Writing .xml file.')
    print(file_data)
    with open('data.xml', 'w') as file:
        xml = xmltodict.unparse(file_data)
        file.write(xml.decode())

def xml_read():
    print(f'Reading .xml file.')
    with open('data.xml', 'r') as file:
        data = xmltodict.parse(file.read())
    return data

def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == '__main__':
    main()
