#include <iostream>

/// \brief      Header-only example class.
class ExClass {
public:
    void Fn(std::string msg) {
        std::cout << "Msg = " << msg << std::endl;
    }

    void Fn(uint32_t number) {
        std::cout << "Number = " << number << std::endl;
    }
};