#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""

# 1046

def find_prime(n1, n2):
    count = 0
    for i in range(n1, n2+1):
        c = bin(i).count("1")
        if is_prime(c):
            count += 1
    return count

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    print '%d is prime!' % n
    return True


def find_prime_list(n1, n2):
    count = 0
    primes =  [2,3,5,7,11,13,17,19,23,29,31]
    for i in range(n1, n2+1):
        if bin(i).count("1") in primes:
            count += 1
    return count

print find_prime_list(10, 15)
















