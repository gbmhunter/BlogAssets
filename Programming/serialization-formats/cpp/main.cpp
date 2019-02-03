#include <chrono>
#include <iostream>
#include <fstream>

#include "csv.h"
#include "json.hpp"

class Person {
    public:
    uint32_t id_;
    std::string name_;
    std::string address_;
    double age_;

    Person(uint32_t id, std::string name,
            std::string address, double age) {
        id_ = id;
        name_ = name;
        address_ = address;
        age_ = age;
    }
};

void csv_read(std::string input_file) {
    std::vector<Person> people;
    io::CSVReader<4> in(input_file);
    in.read_header(io::ignore_missing_column, "id", "name", "address", "age");
    std::string id, name, address, age;
    while(in.read_row(id, name, address, age)) {
        Person person(std::stoi(id), name, address, std::stod(age));
        people.push_back(person);
    }
}

void json_read(std::string input_file) {
    std::ifstream i(input_file);
    nlohmann::json json_data;
    i >> json_data;

    std::vector<Person> json_people;
    for(auto json_person: json_data) {
        Person person(json_person["id"],
                json_person["name"],
                json_person["address"],
                json_person["age"]);
        json_people.push_back(person);
    }
}


int main(){
    
    auto input_file_dir = std::string("../test/input_files/");

    std::chrono::high_resolution_clock::time_point t1;
    std::chrono::high_resolution_clock::time_point t2;

    //============================================================================//
    // CSV
    //============================================================================//

    t1 = std::chrono::high_resolution_clock::now();
    csv_read(input_file_dir + "data.csv");
    t2 = std::chrono::high_resolution_clock::now();
    auto duration_us = std::chrono::duration_cast<
        std::chrono::microseconds>(t2 - t1).count();

    std::cout << "Duration (ms) = " << duration_us/1000.0 << std::endl;

    //============================================================================//
    // JSON
    //============================================================================//
    t1 = std::chrono::high_resolution_clock::now();
    json_read(input_file_dir + "data.json");
    t2 = std::chrono::high_resolution_clock::now();
    duration_us = std::chrono::duration_cast<
        std::chrono::microseconds>(t2 - t1).count();

    std::cout << "Duration (ms) = " << duration_us/1000.0 << std::endl;

}