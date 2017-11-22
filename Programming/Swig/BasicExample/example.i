/* File: example.i */
%module example

%{
#define SWIG_FILE_WITH_INIT
#include "Example.hpp"
%}

int fact(int n);