# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 13:20:50 2015

@author: govert
"""
def count_subana(word):
    substrings = []
    for i in range(len(word)+1):
        for j in range(i+1, len(word)+1):
            substrings.append(''.join(sorted(word[i:j])))
    
    substrings.remove(word)
    substrings.sort()
    print substrings
    final_cnt = 0
    cnt = 0
    for i in range(1, len(substrings)):
        
        if (substrings[i] == substrings[i-1]):
            cnt += 1
            final_cnt += cnt
        else:
            cnt = 0

    return final_cnt


t = int(input())

while(t>0):
    word = raw_input()
    print count_subana(word)
    t-=1
        