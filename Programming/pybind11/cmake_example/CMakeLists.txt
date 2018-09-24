cmake_minimum_required(VERSION 2.8.12)
project(cmake_example)

# The pybind11 repo is a CMake project
add_subdirectory(pybind11)

# src/main.cpp is a pybind11-enabled C++ module
pybind11_add_module(cmake_example src/main.cpp)