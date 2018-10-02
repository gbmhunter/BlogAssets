#include <iostream>
#include <vector>

class BasicTypes { 
    public:

    static std::vector<int> Vector(std::vector<int> input) {
        for (auto number : input) {
            std::cout << number;
        }
        return input;
    }
};