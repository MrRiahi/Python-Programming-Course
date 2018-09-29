# Compute area and environment of circle

import math
import time as tm
from time import time


r = float(input('What is radius :\n'))

area = (math.pi)*(r**2)
environment = 2*(math.pi)*r

print('Area and Environment of Circle is {} and  {}'.format(area, environment))


print('Area :', format(int(area), 'd'), '\t', "Environment :",
      format(environment, 'e'))

