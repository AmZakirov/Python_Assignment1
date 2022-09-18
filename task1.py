# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:13:44 2022

@author: zakir
"""
from time import time,sleep


def decorator_time(f):
    counter = 0
    def wrapper(*args):
        nonlocal counter
        counter += 1
        start_point = time()
        sleep(2)
        f(*args)
        print(f)
        print("Time = " , time() - start_point - 2)
        print("Counts = " , counter)
    return wrapper

@decorator_time
def func(n,i):
    var = i**n
    print("Result 1 = " , var)
    print("\n")
    return
    
    
@decorator_time
def funx(n,i,j):
    var = i**n/j
    print("Result 2 = " , var)
    print("\n")
    return

func(1,1)
func(2,1)
func(10,4)

funx(1,1,3)
funx(2,1,5)
funx(10,4,10)

    