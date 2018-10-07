#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
# resource 
# https://blog.csdn.net/majichen95/article/details/80385188

def can_place_flowers(flowerbed, n):
    if n == 0:
        return True
    flowerbed.insert(0,0)
    flowerbed.append(0)
    count = 0
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            count += 1
    if count >= n:
        return True
    return False

print can_place_flowers([1,0,0,0,1], 2)
print can_place_flowers([1,0,0,0,1], 1)

