import matplotlib.pyplot as plt
import numpy as np


## Define variable
x = np.linspace(-5, 5, 200)
y1 = x**2
y2 = x**3


### Subplot
xlabels = ('x numbers')
ylabels = {'y1' : 'Squared', 'y2' : 'Cubed'}


plt.subplot(1,2,1).plot(x, y1, label = 'Graph1', color = 'r')
plt.xlabel(xlabels[0])
plt.ylabel(ylabels['y1'])
plt.title('Graph1')
plt.legend()


plt.subplot(1,2,2).plot(x, y2, label = 'Graph2', color = 'y')
plt.xlabel(xlabels[0])
ylabel = {'y2' : 'y2 number'}
plt.ylabel(ylabels['y2'])
plt.title('Graph2')
plt.legend()


plt.show()
