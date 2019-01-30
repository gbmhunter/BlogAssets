#!/usr/bin/env python3

from schema import And, Optional, Schema, Use

print('test')

def validate_bands(bands):
    print(f'bands = {bands}')
    return True

test_schema = Schema({
    'number': And(Use(int)),
    Optional('optional_str'): And(Use(str)),
    'bands': validate_bands
})

test_dict = {
    'number': 2,
    'optional_str': 'string',
    'bands': {
        'RED': 0.2
    }
}

test_schema.validate(test_dict)