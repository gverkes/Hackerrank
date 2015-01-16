# -*- coding: utf-8 -*-
"""
Created on Tue Jan 06 10:04:33 2015

@author: govert
"""
import sys

def knapsack(v, w):
    maxi = 0
    cnt = 0
    for i in v:
        cnt+=1
        if (w - i) > 0:
            summ = i + knapsack(v, w-i)
        elif (w - i) == 0:
            summ = i
        else:
            summ = 0
        if summ > maxi:
            maxi = summ
    return maxi
            
            

sys.setrecursionlimit(2100)
t = 1#int(input())

while(t>0):
    params = [1, 2000] #[int(i) for i in raw_input().strip().split()]
    ipt = [1] #[int(i) for i in raw_input().strip().split()]
    print knapsack(ipt, params[1])
    
    t -= 1