# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:45:11 2022

@author: zakir
"""

from time import time , sleep
import inspect

class A:
    
    def __init__(self,func):
        
        self.counter = 0
        self.time = 0.0
        self.func = func

    #Inspecting block
    def inspector(self,file,output):
        #Docstring block
        file.write("\nName: " + str(self.func.__name__))
        file.write("\nType: " + str(type(self.func)))
        file.write("\nSignature: " + str(inspect.signature(self.func)))
        file.write("\nArgs: " +  str(inspect.getfullargspec(self.func)))
        file.write("\nDocumentation: " + str(inspect.getdoc(self.func)))
        file.write("\nSource:")
        file.write("\n")
        file.write(str(inspect.getsource(self.func)))
        file.write("Output: " +  str(output))
        file.write("\n\n")        
        return

    #Timing block
    def timing(self, file, *args):
        global exec_time , fun_name
        t0 = time()
        sleep_time = 0.5
        sleep(sleep_time)
        output = self.func(*args)
        
        self.elapsed_time = time() - t0 - sleep_time
        out_list = [self.func.__name__ ,self.counter ,"counts","in",self.elapsed_time,"sec"]
                
        for item in out_list:
            file.write("%s " %str(item))
        print(*out_list , sep = " ")
        
        exec_time.append(self.elapsed_time)
        fun_name.append(self.func.__name__)
             
        return output
    
    #Call block    
    def __call__(self, *args):
        
        #Counts
        self.counter+=1
        
        
        Var = A.timing(self, file, *args)
        A.inspector(self,file , Var)
        

    

@A
def function1(n,i):
    """
    Sum of first and second parameters
    """
    out = n + i + 0
    return out

    
@A
def function2(n,i):
    """
    Sum of first and second parameters and 8
    """    
    out = n + i + 8
    return out

@A
def function3(n,i):
    """
    Sum of first and second parameters and 16
    """    
    out = n + i + 16
    return out


@A
def function4(n,i):
    """
    Sum of first and second parameters and 10000
    """    
    out = n + i + 10000
    return out

    
Class = A
exec_time , fun_name , rank = [] , [] , [i for i in range(1,5)]

file = open('Output_task3.txt', 'w+')
function1(1,1)
function2(30,10)
function2(10,20)
function2(1,1)
function2(40,20)
function3(1,1)
function4(1,1)
function1(2,1)
file.close()

#Sort functions by executed time and create a dictionary contained the lowest executed time 
Sorted_dict = dict(sorted(zip(exec_time, fun_name)))
Ranking_dict = {}
temp = []
unique_functions = 0
for k , v in Sorted_dict.items():
    if v not in temp:
        unique_functions +=1
        temp.append(v)
        Ranking_dict[k] = v
    


#Inserting function's ranking:
with open("Output_task3.txt", "r") as f:
    contents = f.readlines()

contents.insert(0, "python task3.py\n")
contents.insert(1, "Program | Rank | Time elapsed\n")
for i in range(unique_functions):
    u = 2+i
    contents.insert(u, str(list(Ranking_dict.values())[i]) + "   " + str(rank[i]) + "    " + str(list(Ranking_dict)[i]) + "\n")
contents.insert(6,"\n")

with open("Output_task3.txt", "w") as f:
    contents = "".join(contents)
    f.write(contents)
