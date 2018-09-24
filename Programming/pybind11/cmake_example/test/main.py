import cmake_example
print(f'cmake_example.add(1, 2) = {cmake_example.add(1, 2)}.')

example_class = cmake_example.ExampleClass('Harry')
print(f'example_class.GetName() = {example_class.GetName()}')
example_class.SetName('Bob')
print(f'example_class.GetName() = {example_class.GetName()}')

# This tests C++ writing to std::cout (should appear on console just like python print() statements)
example_class.PrintName()