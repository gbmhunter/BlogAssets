import example

exClass1 = example.ExClass()
print('Sum of [1, 2, 3] = ' + str(exClass1.SumInt([1, 2, 3])))
print('Sum of first 2 of [1, 2, 3] = ' + str(exClass1.SumInt([1, 2, 3], 2)))

print('Sum of [1, 2, 3] = ' + str(exClass1.SumUInt8([1, 2, 3])))
print('Sum of first 2 of [1, 2, 3] = ' + str(exClass1.SumUInt8([1, 2, 3], 2)))

print('Sum of [1, 2, 3] = ' + str(exClass1.SumSpUInt8([1, 2, 3])))
print('Sum of first 2 of [1, 2, 3] = ' + str(exClass1.SumSpUInt8([1, 2, 3], 2)))