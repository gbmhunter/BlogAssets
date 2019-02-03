#include <chrono>
#include <iostream>
#include <fstream>

#include "cpptoml.h"
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

std::vector<Person> csv_read(std::string input_file) {
    std::vector<Person> people;
    io::CSVReader<4> in(input_file);
    in.read_header(io::ignore_missing_column, "id", "name", "address", "age");
    std::string id, name, address, age;
    while(in.read_row(id, name, address, age)) {
        Person person(std::stoi(id), name, address, std::stod(age));
        people.push_back(person);
    }
    return people;
}

void csv_write(std::vector<Person> people, std::string file_path) {
    std::ofstream file;
    file.open(file_path);
    for(auto person: people) {
        file << person.id_ << "," << person.name_ << "," <<
            person.address_ << "," << person.age_ << std::endl;
    }
    file.close();
}

std::vector<Person> json_read(std::string input_file) {
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
    return json_people;
}

void json_write(std::vector<Person> people, std::string file_path) {
    auto json_data = nlohmann::json::array();
    for(auto person: people) {
        auto json_person = nlohmann::json::object();
        json_person["id"] = person.id_;
        json_person["name"] = person.name_;
        json_person["address"] = person.address_;
        json_person["age"] = person.age_;
        json_data.push_back(json_person);
    }

    std::ofstream file(file_path);
    file << json_data << std::endl;
    file.close();
}

std::vector<Person> toml_read(std::string input_file) {
    std::vector<Person> people;
    auto toml_data = cpptoml::parse_file(input_file);
    auto toml_people = toml_data->get_table_array("data");
    for(const auto& toml_person : *toml_people) {
        auto id = toml_person->get_as<int>("id");
        Person person(
            *(toml_person->get_as<uint32_t>("id")),
            *(toml_person->get_as<std::string>("name")),
            *(toml_person->get_as<std::string>("address")),
            *(toml_person->get_as<double>("age")));
        people.push_back(person);
    }
    return people;
}

void toml_write(std::vector<Person> people, std::string file_path) {

    auto toml_people = cpptoml::make_table_array();
    for(auto person : people) {
        auto toml_person = cpptoml::make_table();
        toml_person->insert("id", person.id_);
        toml_person->insert("name", person.name_);
        toml_person->insert("address", person.address_);
        toml_person->insert("age", person.age_);
        toml_people->push_back(toml_person);
    }

    std::ofstream file(file_path);
    file << toml_people;
    file.close();
}

double calc_duration_ms(std::chrono::high_resolution_clock::time_point t1,
    std::chrono::high_resolution_clock::time_point t2) {

    auto duration_us = std::chrono::duration_cast<
        std::chrono::microseconds>(t2 - t1).count();
    return duration_us/1000.0;
}

std::tuple<double, std::vector<Person>> measure_and_repeat_read(
    std::function<std::vector<Person>(std::string)> func,
    std::string file_path) {
    std::vector<double> read_durations_ms;
    auto people = std::vector<Person>();
    for(uint32_t i = 0; i < 3; i++) {
        auto t1 = std::chrono::high_resolution_clock::now();
        people = func(file_path);
        auto t2 = std::chrono::high_resolution_clock::now();
        read_durations_ms.push_back(calc_duration_ms(t1, t2));
    }
    auto min_duration_ms = std::min_element(std::begin(read_durations_ms),
        std::end(read_durations_ms));
    return std::make_tuple(min_duration_ms[0], people);
}

double measure_and_repeat_write(
    std::function<void(std::vector<Person>, std::string)> func,
    std::vector<Person> people,
    std::string file_path) {
    std::vector<double> durations_ms;
    for(uint32_t i = 0; i < 3; i++) {
        auto t1 = std::chrono::high_resolution_clock::now();
        func(people, file_path);
        auto t2 = std::chrono::high_resolution_clock::now();
        durations_ms.push_back(calc_duration_ms(t1, t2));
    }
    auto min_duration_ms = std::min_element(std::begin(durations_ms),
        std::end(durations_ms));
    return min_duration_ms[0];
}

int main(){
    
    auto input_file_dir = std::string("./temp/input_files/");
    auto output_file_dir = std::string("./temp/output_files/");

    auto read_funcs = 
            std::vector<std::function<std::vector<Person>(std::string)>>{
        csv_read,
        json_read,
        toml_read,
    };
    
    read_funcs.push_back(csv_read);
    read_funcs.push_back(json_read);

    auto write_funcs =
        std::vector<std::function<void(std::vector<Person>, std::string)>>{
            csv_write,
            json_write,
            toml_write,
        };

    auto extensions = std::vector<std::string>{
        "csv",
        "json",
        "toml",
    };
    

    std::chrono::high_resolution_clock::time_point t1;
    std::chrono::high_resolution_clock::time_point t2;

    std::vector<double> read_durations_ms;
    std::vector<double> write_durations_ms;
    for(int i = 0; i < extensions.size(); i++) {
        std::cout << "Extension = " << extensions[i] << std::endl;
        auto tuple = measure_and_repeat_read(read_funcs[i],
            input_file_dir + "data." + extensions[i]);
        read_durations_ms.push_back(std::get<0>(tuple));
        std::cout << "Read duration (ms) = " << read_durations_ms[i] << std::endl;

        auto duration_ms = measure_and_repeat_write(
            write_funcs[i],
            std::get<1>(tuple),
            output_file_dir + "data." + extensions[i]);
        write_durations_ms.push_back(duration_ms);
        std::cout << "Write duration (ms) = " << write_durations_ms[i] << std::endl;
    }

}