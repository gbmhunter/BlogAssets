#include <iostream>
#include <pybind11/pybind11.h>

namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

class ExampleClass {
    public:
        ExampleClass(const std::string& name) {
            name_ = name;
        }

        void SetName(const std::string &name) {
            name_ = name;
        }

        const std::string& GetName() {
            return name_;
        }

        void PrintName() {
            std::cout << "Name = " << name_ << std::endl;
        }

    private:
        std::string name_;
};

PYBIND11_MODULE(cmake_example, m) {
    m.doc() = R"pbdoc(
        Pybind11 example plugin
        -----------------------
        .. currentmodule:: cmake_example
        .. autosummary::
           :toctree: _generate
           add
           subtract
    )pbdoc";

    m.def("add", &add, R"pbdoc(
        Add two numbers
        Some other explanation about the add function.
    )pbdoc");

    m.def("subtract", [](int i, int j) { return i - j; }, R"pbdoc(
        Subtract two numbers
        Some other explanation about the subtract function.
    )pbdoc");

    py::class_<ExampleClass>(m, "ExampleClass")
        .def(py::init<const std::string &>())
        .def("SetName", &ExampleClass::SetName)
        .def("GetName", &ExampleClass::GetName)
        .def("PrintName", &ExampleClass::PrintName);

    #ifdef VERSION_INFO
        m.attr("__version__") = VERSION_INFO;
    #else
        m.attr("__version__") = "dev";
    #endif
}