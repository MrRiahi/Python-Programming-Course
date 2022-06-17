import pandas as pd

dic = {'A' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
         'B' : ['one', 'one', 'two', 'two', 'one', 'one'],
         'C' : ['x', 'y', 'x', 'y', 'x', 'y'],
         'D' : [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(dic)

print('df of dic is:\n', df)

df.to_csv('test1.csv', index=False)
df.to_csv('test2.csv', index=True)
df.to_excel('test3.xlsx', sheet_name='Sheet2')

