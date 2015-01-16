# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 18:51:15 2015

@author: govert
"""

import math

def taylor_pi(n):
    sum = 0
    for i in range(2*n):
        sum += (math.pow((-1.),i)/((2.*i)+1.)) #+ 1./(2.*n)
    return 4*sum
        
        
        
for i in range(1, 1000000, 10000):
    print taylor_pi(i)
    print "n=", i, " error=", taylor_pi(i)-math.pi