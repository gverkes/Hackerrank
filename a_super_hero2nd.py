# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 22:12:49 2015

@author: govert
"""


import time
import random

def solver(pows, buls, sub, level):
    best = -1

    if len(pows) == level-1:
        for i in range(len(pows[0])):
            if (pows[level][i] - sub) < 0:
                summ = solver(pows, buls, buls[level][i], level+1)
            else:
                summ = pows[level][i] - sub + solver(pows, buls, buls[level][i], level+1)
            if best < 0:
                best = summ
            if summ < best:
                best = summ
        
    else:
        if (min(pows[level]) - sub) > 0:
            best = min(pows[level])-sub
        else:
            best = 0
    

    
    return best

# Test cases
t = 1#int(input())

while(t > 0):
    #params = [int(i) for i in raw_input().strip().split()]
    
    levels_power = [[random.randint(1,1000) for i in range(5000)] for i in range(100)]#[[int(i) for i in raw_input().strip().split()] for j in range(params[0])]
    levels_bullets = [[random.randint(1,1000) for i in range(5000)] for i in range(100)]#[[int(i) for i in raw_input().strip().split()] for j in range(params[0])]
 
    start = time.clock()
    print solver(levels_power, levels_bullets, 0, 0)
    end = time.clock()
    print "%.2gs" % (end-start)
#    for i in range(params[0]-1, 0, -1):
#        min_val = min(levels_power[i])
#        c_vals = [min_val - x for x in levels_bullets[i-1]]
#        for j in range(len(c_vals)):
#            if c_vals[j] > 0:
#                levels_power[i-1][j] += c_vals[j]
                
#    print min(levels_power[0])
        
    t-=1