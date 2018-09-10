import example

exClass1 = example.ExClass()

print('Calling C++ code (exClass1.Factorial(4)) from python...')
print(f'result = {exClass1.Factorial(4)}')