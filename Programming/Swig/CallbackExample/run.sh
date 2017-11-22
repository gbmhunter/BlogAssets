#!/usr/bin/env bash

swig -Wall -c++ -python example.i
g++ -shared -fPIC Example.cpp example_wrap.cxx -o _example.so -I/usr/include/python3.5m/
python3 test.py
rm -rf example.py example.pyc _example.so example_wrap.cxx __pycache__/ 