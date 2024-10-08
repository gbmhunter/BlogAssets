#!/usr/bin/env bash

# Fail on error
set -e

# Make directories needed by C++ and Python code
mkdir -p temp
mkdir -p temp/input_files
mkdir -p temp/proto_py
mkdir -p temp/proto_cpp
touch temp/proto_py/__init__.py

mkdir -p temp/output_cpp
mkdir -p temp/output_py
mkdir -p temp/stats

# Compile the .proto protobuf files
echo 'Running the protobuf compiler...'
protoc -I=proto/ --python_out=temp/proto_py/ --cpp_out=temp/proto_cpp proto/PBPeople.proto proto/PBPerson.proto

# Create input files for testing
python ./python_code/create_input.py

# Perform read/write serial format testing in C++
echo 'Compiling C++ code...'
g++ -pthread ./cpp/main.cpp ./cpp/tinyxml2.cpp ./temp/proto_cpp/PBPeople.pb.cc ./temp/proto_cpp/PBPerson.pb.cc -lyaml-cpp -lprotobuf -o ./temp/cpp.out
./temp/cpp.out

# Perform read/write serial format testing in Python
python ./python_code/perform_tests.py

# Perform analysis
python ./python_code/analysis.py