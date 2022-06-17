# Compute area and environment of circle

import math
##import numpy as np
##from time import time


r = float(input('What is radius :\n'))

area = (math.pi)*(r**2)
environment = 2*(math.pi)*r

print('Area :\t', area, '\n', 'environment :\t', environment, sep='')


print('Area :', format(area, '1,.2f'), '\t', "environment :",
      format(environment, '.4f'))
print('Area :', format(int(area), 'd'), '\t', "environment :",
      format(environment, 'e'))
