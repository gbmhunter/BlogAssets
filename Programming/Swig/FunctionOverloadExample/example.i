/* File: example.i */
%module example

%include "stdint.i"
%include "std_string.i"

%{
    #include "Example.hpp"
%}

%include "Example.hpp"