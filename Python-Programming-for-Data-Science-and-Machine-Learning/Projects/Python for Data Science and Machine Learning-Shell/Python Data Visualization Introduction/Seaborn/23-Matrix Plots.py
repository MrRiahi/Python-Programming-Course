import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset('tips')
tips

### Convert data to matrix
MatTips = tips.corr()

MatTips


sns.heatmap(MatTips, annot = False)
plt.show()

sns.heatmap(MatTips, annot = True, linecolor = 'white', linewidth = 1, cmap = 'coolwarm')

plt.show()
