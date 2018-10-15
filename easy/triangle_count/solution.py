#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""


def enu(nums):
    rnum = 0
    for p1 in range(len(nums) - 2):
        print('p1: ', p1)
        for p2 in range(p1+1, len(nums) - 1):
            print('p2: ', p2)
            max_n = nums[p1] + nums[p2]
            min_n = abs(nums[p1] - nums[p2])
            for p3 in range(p2+1, len(nums)):
                print('p3: ', p3)
                if nums[p3] in range(min_n + 1, max_n):
                    print('bingo! ', nums[p1], nums[p2], nums[p3])
                    rnum += 1
    return rnum
    



def enu2(nums):
    # example [2,2,3,4]
    res = 0
    n = len(nums)
    for p1 in range(n-2):
        for p2 in range(p1+1, n-1):
            max_p, min_p = nums[p1] + nums[p2], abs(nums[p1] - nums[p2])
            for p3 in range(p2+1, n):
                if min_p < nums[p3] < max_p:
                    print('bingo! ', nums[p1], nums[p2], nums[p3])
                    res += 1
    return res



# sort
# find limit



def with_sort(nums):
    sorted(nums)
    res, n = 0, len(nums)
    flag = False
    for p1 in range(n-2):
        for p2 in range(p1+1, n-1):
            max_p = nums[p1] + nums[p2]
            pleft, pright = p2+1, n-1
            while pright >= pleft:
                if nums[pright] < max_p:
                    flag = True
                    break
                if nums[pright] >= max_p:
                    pright -= 1
            if flag:
               print('bingo! ', nums[p1], nums[p2], nums[pright])
               print('pright, pleft! ', pright, pleft)
               res += pright - pleft + 1
    return res

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



print with_sort([7,4,6,3])# [2,2,3,4]


















