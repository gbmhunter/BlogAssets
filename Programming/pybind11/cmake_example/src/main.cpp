#include <iostream>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "BasicTypes.hpp"
#include "ExampleClass.hpp"

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

void init_ex1(py::module &m) {
    // Attaches a lone predefined function to the Python module 
    m.def("add", add);

    // This shows you how C++ lambdas can be used to create Python-callable
    // functions on-the-fly
    m.def("subtract", [](int a, int b) { return a - b; });
}

void init_ex2(py::module &m) {
    // This adds a C++ class to the Python module
    py::class_<ExampleClass>(m, "ExampleClass")
        .def(py::init<const std::string &>())
        .def("SetName", &ExampleClass::SetName)
        .def("GetName", &ExampleClass::GetName)
        .def("PrintName", &ExampleClass::PrintName);
}

void init_basic_types(py::module &m) {
    py::class_<BasicTypes>(m, "BasicTypes")
        .def("Vector", &BasicTypes::Vector);
}

PYBIND11_MODULE(cmake_example, m) {
    init_ex1(m);
    init_ex2(m);
    init_basic_types(m);
}