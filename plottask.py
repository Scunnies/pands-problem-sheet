# this program plots the functions f(x)=x, g(x)=x2 and h(x)=x3 
# in the range [0, 4] on the one set of axes
# Author: Eleanor Sammon

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 4, 250) # I researched how to plot a smooth curve

# the basic calculations to be plotted
y = x
y2 = x*2    
y3 = x**3

# the fun part! presenting the output in an attractive way
plt.plot(x, y, 'c-', label = "f(x) = x")
plt.plot(x, y2, 'm--', label = "g(x) = x2")
plt.plot(x, y3, 'y:', label = "h(x) = x3")
plt.grid(color = 'b', linestyle = '--', linewidth = 0.25)

# adding labels and a legend for clarity
plt.title('Week 8 Task - Plotting Functions', loc = 'right')
plt.xlabel('X AXIS')
plt.ylabel('Y AXIS')
plt.legend()

plt.show()


# https://www.w3schools.com/python/matplotlib_intro.asp
# https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
# https://www.adamsmith.haus/python/answers/how-to-plot-a-smooth-line-with-matplotlib-in-python
# https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html