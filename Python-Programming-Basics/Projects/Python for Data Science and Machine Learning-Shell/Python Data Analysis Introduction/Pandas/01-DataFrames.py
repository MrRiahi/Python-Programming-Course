import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(data = randn(5, 4), index = ['A', 'B', 'C', 'D', 'E'],
                  columns = ['W', 'A', 'Y', 'Z'])

print('Data frame is:\n', df)

print('')

print('''W's column Elements is:\n''', df['W'])

print('')

print('''W's and Z's columns Elements is:\n''', df[['W', 'Z']])

print('')

df['new'] = df['W']+df['Y']
print('Data frame with new column is:\n', df)

print('')

df.drop(labels='new', axis=1, inplace=True)
print('Data frame without new column is:\n', df)

print('')

print('Drop data frame with labels A and axis 0:\n', df.drop(labels='A', axis=0))

print('')

print('Drop data frame with labels A and axis 1:\n', df.drop(labels='A', axis=1))

print('')

print('Shape of data frame is:', df.shape)

print('')

### print(df['B'])
print('''C's index elements is:\n''', df.loc['C'])

print('')

print('''Second index elements is:\n''', df.iloc[2])

print('')

print('Element of B index and Y column is:', df.loc['B', 'Y'])

print('')

print('Elements of A and B indices and W and Y columns is:\n',
      df.loc[['A', 'B'], ['W', 'Y']])
