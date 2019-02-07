#!/usr/bin/env bash

# Fail on error
set -e

# Make directories needed by C++ and Python code
mkdir -p temp
mkdir -p temp/input_files
mkdir -p temp/output_cpp
mkdir -p temp/output_py
mkdir -p temp/stats

# Create input files for testing
python ./python_code/create_input.py

# Perform read/write serial format testing in C++
echo 'Compiling C++ code...'
g++ -pthread ./cpp/main.cpp ./cpp/tinyxml2.cpp -lyaml-cpp -o ./temp/cpp.out
./temp/cpp.out

# Perform read/write serial format testing in Python
python ./python_code/perform_tests.py

# Perform analysis
python ./python_code/analysis.py