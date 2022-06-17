import numpy as np


array1 = np.array([1, 2, 3])

print('Second elemnt of array1 is:', array1[1])

array2 = np.array([[6, 7, 8], 
                   [1, 2, 3],
                   [9, 3, 2]])

print('--------------------------------')




print('Rows of array2 is:')
for row in array2:
    print(row)

print('')

print('Columns of array2 is:')
for col in array2.transpose():
    print(col)


print('--------------------------------')


array3 = np.arange(30).reshape(2, 15)
print('Array3 is:\n', array3)

print('')

print('Number of rows and columns respectively is {} and {}'
      .format(np.size(array3, axis = 0),np.size(array3, axis = 1)), '\n')

print('')

print('Shape of array3 is:', array3.shape)

print('--------------------------------')

array5 = np.array([[1, 2], [3, 4]])
array6 = np.array([[5, 6], [7, 8]])
print('Array5 is:\n', array5)
print('')
print('Array6 is:\n', array6)
print('')

array7 = array5.dot(array6)
print('Matrix Product of array5 to array6 is:\n', array7)

print('--------------------------------')

array8 = np.array([[1, 2], 
                   [3, 4],
                   [5, 6]])

print('Sum of each columns is:\n', array8.sum(axis = 0))
print('')
print('Sum of each rows is:\n',array8.sum(axis = 1))
print('')
print('Sum of each elements is:\n', array8.sum())

print('--------------------------------')
