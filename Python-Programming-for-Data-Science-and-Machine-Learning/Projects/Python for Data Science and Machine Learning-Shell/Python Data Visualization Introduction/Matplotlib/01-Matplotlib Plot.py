import matplotlib.pyplot as plt
import numpy as np


## Define variable
x = np.linspace(0, 5, 100)
y1 = x**2
y2 = x**3

### Plot
plt.plot(x, y1)
plt.plot(x, y2)

##plt.subplot(1,2,1).plot(x1, y1, label = 'First graph')
##plt.subplot(1,2,2).plot(x2, y2, label = 'Second graph')

xlabel = ('x number')
plt.xlabel(xlabel)

ylabel = {'y' : 'y number'}
plt.ylabel(ylabel['y'])

plt.title('My\n Graph')

##plt.xlim([-2, 6])
##plt.ylim([-10, 130])

labels = ('Squared', 'Cubed')
plt.legend(labels)
##plt.legend()

plt.show()

##plt.savefig('MyFig.png', dpi=100)
