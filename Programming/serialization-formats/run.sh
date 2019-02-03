#!/usr/bin/env bash

# Fail on error
set -e

# Make directories needed by C++ and Python code
mkdir -p temp
mkdir -p temp/input_files
mkdir -p temp/output_files
mkdir -p temp/stats

# Create input files for testing
python ./python_code/create_input.py

# Perform read/write serial format testing in C++
g++ -pthread ./cpp/main.cpp ./cpp/tinyxml2.cpp -o ./temp/cpp.out
./temp/cpp.out

# Perform read/write serial format testing in Python
python ./python_code/perform_tests.py