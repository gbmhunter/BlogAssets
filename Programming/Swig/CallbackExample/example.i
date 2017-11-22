%module(directors="1") example

%feature("director") ICallback;

%{
#include "Example.hpp"
%}

%include "Example.hpp"