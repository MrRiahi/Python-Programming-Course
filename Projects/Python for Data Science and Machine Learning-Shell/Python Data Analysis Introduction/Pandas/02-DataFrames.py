import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(data=randn(5, 4), index=['A', 'B', 'C', 'D', 'E'],
                  columns=['W', 'X', 'Y', 'Z'])

print('Head of df is:\n', df.head(n=1))

print('--------------------------')

Booleandf = df > 0
print('Elements of df that is greater than 0 is:\n', Booleandf)
print('')
print(df[Booleandf])
print('')
print(df[df > 0])

print('--------------------------')

print('Elements of column W that is greater than 0 is:\n', df['W'] > 0)
print('')
print(df[df['W'] > 0])
##print(df[df['Z'] < 0])

print('--------------------------')

print('Elements of in X and Y  that are thier corresponding indices in W are greater than 0 is:\n '
      , df[df['W'] > 0][['X', 'Y']])

''' Another way for above code is
   boolser = df['W'] > 0
   result = df[boolser]
   MyCols = ['X', 'Y']
   result[MyCols]
'''
print('--------------------------')

print('Elements of indices that are greater than 0 in W and greater then 1 in Y is:\n'
      , df[(df['W'] > 0) & (df['Y'] > 1)])

print('--------------------------')

print('Count of the elements of in X is:\n', df['X'].value_counts())
print('')
print('Sum of the elements of in Y is:\n', df['Y'].sum())

