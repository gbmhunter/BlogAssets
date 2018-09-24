class ExampleClass {
    public:
        ExampleClass(const std::string& name) {
            name_ = name;
        }

        void SetName(const std::string &name) {
            name_ = name;
        }

        const std::string& GetName() {
            return name_;
        }

        void PrintName() {
            std::cout << "Name = " << name_ << std::endl;
        }

    private:
        std::string name_;
};
