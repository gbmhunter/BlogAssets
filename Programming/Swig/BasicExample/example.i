/* File: example.i */
%module example

%{
    #define SWIG_FILE_WITH_INIT
    #include "Example.hpp"
%}

%include "Example.hpp"