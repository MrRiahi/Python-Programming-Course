import numpy as np
import matplotlib.pyplot as plt


normal =  np.random.randn(10000000, 1)


plt.hist(normal, bins = 1000, label = 'Histogram', rwidth = 0.8)
plt.xlabel('Bins')
plt.ylabel('Counts')
plt.title('Histogram Graph')
plt.legend()

plt.show()
