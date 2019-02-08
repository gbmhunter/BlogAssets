import csv
import json
import random
import toml
import yaml
import xml.etree.cElementTree as ET
import string
import os

# These .proto files are created dynamically by the run.sh script
sys.path.insert(0, os.path.abspath('./temp/'))
from proto_py import people_pb2

# SCRIPT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
# OUTPUT_DIR = os.path.join(SCRIPT_DIR, '..', 'temp', 'output_files_python')
# print(SCRIPT_DIR)

def string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def csv_read(file_path):
    print(f'Reading .csv file.')
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for i, person in enumerate(csv_reader):
            if i == 0:
                continue
            data.append({
                'id': person[0],
                'name': person[1],
                'address': person[2],
                'age': person[3],
            }) 
    return data

def csv_write(file_data, file_path):
    # print(f'Writing .csv file. file_data = {file_data}')
    with open(file_path, 'w') as file:
        csv_writer = csv.writer(file, delimiter=',')
        # Write header row
        csv_writer.writerow(file_data[0].keys())
        for person in file_data:
            csv_writer.writerow(person.values())

def json_write(file_data, file_path):
    with open(file_path, 'w') as file:
        json.dump(file_data, file)

def json_read(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def protobuf_write(file_data, file_path):
    print(f'Writing .protobuf file.')

    for person in file_data:

    with open(file_path, 'w') as file:
        json.dump(file_data, file)

def protobuf_read(file_path):
    print(f'Writing .json file.')
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def toml_write(file_data, file_path):
    print(f'Writing .toml file.')
    with open(file_path, 'w') as file:
        toml.dump({ 'data': file_data }, file)

def toml_read(file_path):
    print(f'Reading .toml file.')
    with open(file_path, 'r') as file:
        data = toml.load(file)
    return data['data']

def yaml_write(file_data, file_path):
    print(f'Writing .yaml file.')
    with open(file_path, 'w') as file:
        yaml.dump(file_data, file)

def yaml_read(file_path):
    print(f'Reading .yaml file.')
    with open(file_path, 'r') as file:
        data = yaml.load(file)
    return data

def xml_write(file_data, file_path):
    print(f'Writing .xml file.')

    xml_people = ET.Element('people')
    for person in file_data:
        xml_person = ET.SubElement(xml_people, 'person')
        for key, value in person.items():
            xml_element = ET.SubElement(xml_person, str(key))
            xml_element.text = str(value)

    tree = ET.ElementTree(xml_people)
    tree.write(file_path)

def xml_read(file_path):
    tree = ET.parse(file_path)
    xml_people = tree.getroot()

    people = []
    for xml_person in xml_people:
        person = {}
        for xml_person_property in xml_person:
            person[xml_person_property.tag] = xml_person_property.text
        people.append(person)

    return people