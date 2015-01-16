# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 22:12:49 2015

@author: govert
"""
from operator import sub


# Test cases
t = int(input())

while(t > 0):
    params = [int(i) for i in raw_input().strip().split()]
    levels_power = [[int(i) for i in raw_input().strip().split()] for j in range(params[0])]
    levels_bullets = [[int(i) for i in raw_input().strip().split()] for j in range(params[0])]
    
    print "Powers: ", levels_power
    print "Bullets: ", levels_bullets

    print zip(levels_power, levels_bullets)
    henkie = [[i - j for i, j in zip(a, b)] for a, b in zip(levels_power, levels_bullets)]
    print henkie
    #print "Power-Bullets: ", [a - b for a, b in zip(levels_power, levels_bullets)]
    t-=1