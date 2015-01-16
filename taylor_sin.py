# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 20:54:08 2015

@author: govert
"""
import math
import matplotlib.pyplot as plt
import numpy as np

def taylor_sin(x, n):
    sum = 0
    for i in xrange(n+1):
        sum += (math.pow((-1.), i)/math.factorial(2.*i+1.)) * np.power(x, (2.*i+1.))
    return sum
        


t1 = np.linspace(-math.pi,math.pi, 200)
y1 = taylor_sin(t1, 5)
y2 = np.sin(t1)

plt.plot(t1,y1, 'r-')
plt.plot(t1,y2, 'b-')

plt.legend(['taylor_sin', 'sin'])
plt.xlabel('t')
plt.ylabel('y(t)');
plt.axis([-math.pi, math.pi, -1.2, 1.2])
plt.show()