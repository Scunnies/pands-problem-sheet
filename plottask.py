# this program plots the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes
# Author: Eleanor Sammon

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0.0,4.0) 
y = x
y2 = x*2    
y3 = x**3

plt.plot(x, y)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()


# https://www.w3schools.com/python/matplotlib_intro.asp
# https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html