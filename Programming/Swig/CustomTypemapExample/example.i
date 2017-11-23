/* File: example.i */
%module example

%include "typemaps.i"
%include "std_vector.i"
%include "stdint.i"

namespace std {
    // A vector of ints can be taken care of with the provided
    // templates, but we will have to create type map for vector
    // of uint8_t (see below)
    %template(IntVector) vector<int>;    
}

//================================//
//===== std::vector<uint8_t> =====//
//================================//

// Convert from Python --> C
%typemap(in) std::vector<uint8_t, std::allocator<uint8_t>> {  
  auto temp = std::vector<uint8_t>();
  for(int i = 0; i < PyList_Size($input); i++) {
    temp.push_back(PyInt_AsLong(PyList_GetItem($input, i)));
  }
  $1 = temp;  
}

// This typecheck allows for function overloads with std::vector<uint8_t>
// Copy typecheck for std::vector<int>
%typemap(typecheck) std::vector<uint8_t, std::allocator<uint8_t>> = std::vector<int>;

//=================================================//
//===== std::shared_ptr<std::vector<uint8_t>> =====//
//=================================================//

// Convert from Python --> C
%typemap(in) std::shared_ptr<std::vector<uint8_t, std::allocator<uint8_t>>> {  
  auto temp = std::make_shared<std::vector<uint8_t>>();
  for(int i = 0; i < PyList_Size($input); i++) {
    temp->push_back(PyInt_AsLong(PyList_GetItem($input, i)));
  }
  $1 = temp;
}

// This typecheck allows for function overloads with std::vector<uint8_t>
// Copy typecheck for std::vector<int>
%typemap(typecheck) std::shared_ptr<std::vector<uint8_t, std::allocator<uint8_t>>> = std::vector<int>;

%{
    #include "Example.hpp"
%}

%include "Example.hpp"