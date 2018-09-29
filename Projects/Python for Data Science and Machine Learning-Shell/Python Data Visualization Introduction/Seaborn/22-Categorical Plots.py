import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np




tips = sns.load_dataset('tips')
tips.head()



tips.info()



sns.barplot(x='sex', y='total_bill', data=tips)


sns.countplot(x='sex', data=tips)


sns.factorplot(x='sex', y='total_bill', data=tips, kind='bar')


sns.factorplot(x='sex', data=tips, kind='count')

plt.show()

