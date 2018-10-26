import json
from enum import Enum

import jsonpickle

class MyEnum():
    ENUM_1 = 1
    ENUM_2 = 2

# Dictionaries with enums as keys can be hard to serialize/deserialize
my_dict = {
    MyEnum.ENUM_1: 'foo',
    MyEnum.ENUM_2: 'bar',
}

def test():

    serialized_obj =jsonpickle.encode(my_dict)

    print(serialized_obj)

    deserialized_obj = jsonpickle.decode(serialized_obj)

    # This will fail, jsonpickle doesn't support enums
    assert(deserialized_obj[MyEnum.ENUM_1] == 'foo')

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return {"__enum__": str(obj)}
        return json.JSONEncoder.default(self, obj)

def as_enum(d):
    if "__enum__" in d:
        name, member = d["__enum__"].split(".")
        return getattr(PUBLIC_ENUMS[name], member)
    else:
        return d

def test2():
    ser_obj = json.dumps(my_dict, cls=EnumEncoder)

    print(ser_obj)

if __name__ == '__main__':
    #test()

    test2()
