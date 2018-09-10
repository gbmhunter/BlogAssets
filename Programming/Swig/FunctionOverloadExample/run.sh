#!/usr/bin/env bash

swig -Wall -c++ -python example.i
g++ -shared -fPIC example_wrap.cxx -o _example.so -I/opt/conda/include/python3.6m/
python3 test.py
rm -rf example.py example.pyc _example.so example_wrap.cxx __pycache__/ 