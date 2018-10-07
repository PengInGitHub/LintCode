#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""

# resource
# https://github.com/Zhenye-Na/lintcode/tree/master/2.%20Easy/166.%20Nth%20to%20Last%20Node%20in%20List
# https://www.jianshu.com/p/7c77edfe55a8

# 166. Nth to Last Node in List

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        

def NthLast(head, n):
    if not head or n <= 0:
        return None
    
    # test if n is out of bound
    first, num = head, 1
    while first.next:
        num += 1
    if n > num:
        return None
    
    right = head
    while n>1:
        right = right.next
        n -= 1
    
    left = head
    while right.next:
        left = left.next
        right = right.next
    
    return left


def NthLastSimple(head, n):
    if not head or n <= 0:
        return None
    slow, fast = head, head
    for _ in range(n):
        fast = fast.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    return slow


















