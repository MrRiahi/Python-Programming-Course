import pandas as pd

df1 = pd.read_csv('test1.csv')
print(df1)

print('-----------------')

df2 = pd.read_excel('test3.xlsx', sheet_name = "Sheet2")
print(df2)



