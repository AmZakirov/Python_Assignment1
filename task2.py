# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 14:49:26 2022

@author: zakir
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:13:44 2022

@author: zakir
"""
from time import time,sleep
from datetime import datetime
import inspect


def decorator_time_documentation(f):
    counter = 0
    def wrapper(*args):
        nonlocal counter
        counter += 1
        start_point = time()
        sleep(2)
        
        try:
            f(*args)
            out_list = [f.__name__ ,counter ,"counts","in",time() - start_point - 2,"sec"]
            print(*out_list , sep = " ")
            
            #Docstring block
            print("\nName: " , f.__name__)
            print("\nType: " , type(f))
            print("\nSignature: " , inspect.signature(f))
            print("\nArgs: " , inspect.getfullargspec(f))
            print("\nDocumentation: ", inspect.getdoc(f))
            print("\nSource:")
            print(inspect.getsource(f))
            print("Output: ", var)
        
        except Exception as err: 
            print(err)
            now =datetime.now()
            time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            log_file.write("Error time: " + time_str + "\n")
            log_file.write( str(f.__name__) + ": " + str(err) + "\n")
            
    return wrapper

@decorator_time_documentation
def func(n,i):
    """
    This function raises first parameter to a power of the second parameter
    """
    global var
    var = i**n
    return
    
log_file = open('log_task2.txt', 'w+')

func(4,2)
func("k",3)
func(1)

log_file.close()
    