import seaborn as sns
import matplotlib.pyplot as plt



tips = sns.load_dataset('tips')


tips.head()

sns.distplot(tips['total_bill'])

sns.distplot(tips['total_bill'], kde=False)


sns.kdeplot(tips['total_bill'])


sns.jointplot(x = 'total_bill', y = 'tip', data=tips)


plt.scatter(x='total_bill', y='tip', data = tips)


sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')


sns.pairplot(tips)


sns.pairplot(tips, hue='sex')


sns.pairplot(tips, hue='sex', palette='coolwarm')


plt.show()
