import csv
import json
import random
import toml
import yaml
import xml.etree.cElementTree as ET
import string
import os

SCRIPT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, '..', 'test', 'input_files')
print(SCRIPT_DIR)

def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def csv_write(file_data):
    print(f'Writing .csv file.')
    with open(os.path.join(OUTPUT_DIR, 'data.csv'), 'w') as file:
        csv_writer = csv.writer(file, delimiter=',')
        # Write header row
        csv_writer.writerow(file_data[0].keys())
        for person in file_data:
            csv_writer.writerow(person.values())

def csv_read():
    print(f'Reading .csv file.')
    data = []
    with open(os.path.join(OUTPUT_DIR, 'data.csv'), 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for person in csv_reader:
             data.append(person) 
    return data

def json_write(file_data):
    print(f'Writing .json file.')
    with open(os.path.join(OUTPUT_DIR, 'data.json'), 'w') as file:
        json.dump(file_data, file)

def json_read():
    print(f'Writing .json file.')
    with open(os.path.join(OUTPUT_DIR, 'data.json'), 'r') as file:
        data = json.load(file)
    return data

def toml_write(file_data):
    print(f'Writing .toml file.')
    with open(os.path.join(OUTPUT_DIR, 'data.toml'), 'w') as file:
        toml.dump({ 'data': file_data }, file)

def toml_read():
    print(f'Reading .toml file.')
    with open(os.path.join(OUTPUT_DIR, 'data.toml'), 'r') as file:
        data = toml.load(file)
    return data

def yaml_write(file_data):
    print(f'Writing .yaml file.')
    with open(os.path.join(OUTPUT_DIR, 'data.yaml'), 'w') as file:
        yaml.dump(file_data, file)

def yaml_read():
    print(f'Reading .yaml file.')
    with open(os.path.join(OUTPUT_DIR, 'data.yaml'), 'r') as file:
        data = yaml.load(file)
    return data

def xml_write(file_data):
    print(f'Writing .xml file.')

    xml_people = ET.Element('people')
    for person in file_data:
        xml_person = ET.SubElement(xml_people, 'person')
        for key, value in person.items():
            xml_element = ET.SubElement(xml_person, str(key))
            xml_element.text = str(value)

    tree = ET.ElementTree(xml_people)
    tree.write(os.path.join(OUTPUT_DIR, 'data.xml'))

def xml_read():
    tree = ET.parse(os.path.join(OUTPUT_DIR, 'data.xml'))
    xml_people = tree.getroot()

    people = []
    for xml_person in xml_people:
        person = {}
        for xml_person_property in xml_person:
            person[xml_person_property.tag] = xml_person_property.text
        people.append(person)

    return people