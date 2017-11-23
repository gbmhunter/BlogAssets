#include <cstdint>
#include <memory>
#include <vector>

class ExClass {
public:
    int SumInt(std::vector<int> array);
    int SumInt(std::vector<int> array, uint32_t numElements);

    int SumUInt8(std::vector<uint8_t> array);
    int SumUInt8(std::vector<uint8_t> array, uint32_t numElements);

    int SumSpUInt8(std::shared_ptr<std::vector<uint8_t>> array);
    int SumSpUInt8(std::shared_ptr<std::vector<uint8_t>> array, uint32_t numElements);
};
