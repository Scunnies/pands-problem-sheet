# this program plots the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes
# Author: Eleanor Sammon

import matplotlib.pyplot as plt
import numpy as np


xpoints = np.arange(0,5) 
ypoints = np.arange(0,5)

xSquared = xpoints * xpoints


plt.plot(xpoints, ypoints, xSquared)
plt.show()
