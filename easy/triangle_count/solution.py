#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
def triangle_count(my_list):
    # 找出这样的三个数字 使得任意两个数字之和都大于第三个数字
    # 三个数字之中 如果较小的两个之和大于第三个 那么任意两个数字之和都大于第三个
    # 先确定两个数 将这两个数的和作为目标值 然后用二分查找快速确定第一个小于目标值的数
    # 找到这个临界值 那么之前一直到第二个较小数（j) 位置之间的数 都满足题意 直接加起来即可
    
    sorted(my_list)
    res, n = 0, len(my_list)
    for i in range(n):
        for j in range(n):
            j = i+1
            sum, left, right = i + j, j+1, n
            while left < right:
                mid = left + (right-left)/2
                if my_list[mid] < sum:
                    left = mid + 1
                else:
                    right = mid
            res += right -1 - j
    return res

print triangle_count([2,2,3,4])