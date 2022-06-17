import pandas as pd
import numpy as np

# Read Salaries dataset
SalaryDF = pd.read_csv('Salaries.csv', low_memory=False)

# Get Indices of Salaries dataset
Indices = SalaryDF.columns
print(Indices)

print('-------------------------')

# Get head of Salaries dataset with n=1
head = SalaryDF.head(n=1)
print(head)

print('-------------------------')

# Get Salaries dataset informations
info = SalaryDF.info()
print(info)

print('-------------------------')

# Compute the average of  BasePay
mean = SalaryDF['BasePay'].mean()
print(mean)

print('-------------------------')

# Find the job of JOSEPH DRISCOLL
job = SalaryDF[SalaryDF['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
print(job)

''' Question: what is TotalPayBenefits of OSEPH DRISCOLL?'''

print('-------------------------')

# Who got the most TotalPayBenefits?
NameofMaxBenefit = SalaryDF[SalaryDF['TotalPayBenefits'] ==
                            SalaryDF['TotalPayBenefits'].max()]['EmployeeName']
print(NameofMaxBenefit)
