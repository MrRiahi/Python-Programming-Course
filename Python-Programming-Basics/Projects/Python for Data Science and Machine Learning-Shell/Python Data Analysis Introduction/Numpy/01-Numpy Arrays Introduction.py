import numpy as np


array = np.arange(start = 0, stop = 25, step = 1, dtype = 'complex')
print('Arange array is:\n', array, '\n')

print('Reshape array is:\n', array.reshape(5, 5))

print('--------------------------')

zeros = np.zeros((2, 3), dtype='int')
print('Zeros matrix is:\n', zeros)

print('--------------------------')

linspace = np.linspace(start = 0, stop = 5, num=11, endpoint=True, dtype = 'float')
print('Linspace array is:\n', linspace)

print('--------------------------')

eye = np.eye(5)
print('Eye matrix is:\n', eye)

print('--------------------------')

UniformRand = np.random.rand(5, 2)
print('Uniform random is:\n', UniformRand)

print('--------------------------')

NormalRand = np.random.randn(5)
print('Normal random is:\n', NormalRand)

print('--------------------------')

IntRand = np.random.randint(low = 1, high = 10, size = 7)
print('Integer random is:\n', IntRand)

print('maximum of IntRand is:', IntRand.max())
print('Argoman maximum of   IntRand is:', IntRand.argmax())
print('minimum of IntRand is:', IntRand.min())
print('Argoman mainimum of   IntRand is:',IntRand.argmin())

print('--------------------------')


