#!/usr/bin/env bash

# Fail on error
set -e

mkdir -p temp
mkdir -p temp/input_files

# Create input files for testing
python ./python_code/create_input.py

g++ -pthread ./cpp/main.cpp -o ./temp/cpp.out
./temp/cpp.out