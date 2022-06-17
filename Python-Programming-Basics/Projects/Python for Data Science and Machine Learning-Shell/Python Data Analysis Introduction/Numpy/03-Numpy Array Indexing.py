import numpy as np


array1 = np.arange(start = 0, stop = 30)

print('First five element of array1 is:\n', array1[:5])

print('')

SliceArr = array1[:6]
print('SliceArr is:\n', SliceArr)

print('')

SliceArr[:] = 99
print('New SliceArr is:\n', SliceArr)
print('')
print('Array1 is:\n', array1)


print('------------------------')


array2 = np.array([[6, 7, 8], 
                   [1, 2, 3],
                   [9, 3, 2]])

# Question: How access to number 9 in array2

print('Third element in first columns is:', array2[2][0])

print('')

print(array2[:2, 1:])


print('------------------------')


array3 = np.arange(30).reshape(2, 15)
temp = array3 > 19
print('Element of greater than 4 in array5 is:\n', array3[temp])

print('')

array4 = array3.copy()
array4[temp] = -1
print('Array4 is:\n', array4)
