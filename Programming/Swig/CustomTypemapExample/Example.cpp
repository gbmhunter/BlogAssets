
#include "Example.hpp"

int ExClass::SumInt(std::vector<int> array) {
    int sum = 0;
    for(auto const& val : array) {
        sum += val;
    }
    return sum;
}

int ExClass::SumInt(std::vector<int> array, uint32_t numElements) {
    int sum = 0;
    uint32_t index = 0;
    for(auto const& val : array) {        
        sum += val;
        index++;
        if(index == numElements)
            break;
    }
    return sum;
}

int ExClass::SumUInt8(std::vector<uint8_t> array) {
    int sum = 0;
    for(auto const& val : array) {
        sum += val;
    }
    return sum;
}

int ExClass::SumUInt8(std::vector<uint8_t> array, uint32_t numElements) {
    int sum = 0;
    uint32_t index = 0;
    for(auto const& val : array) {        
        sum += val;
        index++;
        if(index == numElements)
            break;
    }
    return sum;
}

int ExClass::SumSpUInt8(std::shared_ptr<std::vector<uint8_t>> array) {
    int sum = 0;
    for(auto const& val : *array) {
        sum += val;
    }
    return sum;
}

int ExClass::SumSpUInt8(std::shared_ptr<std::vector<uint8_t>> array, uint32_t numElements) {
    int sum = 0;
    uint32_t index = 0;
    for(auto const& val : *array) {        
        sum += val;
        index++;
        if(index == numElements)
            break;
    }
    return sum;
}