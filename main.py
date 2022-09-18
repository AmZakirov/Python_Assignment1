# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:44:47 2022

@author: 
"""

l0 = [i for i in range(10)]
print("Initial list",l0)

"Function 1. Raise elements of the list to 3 degree"
def func1(l):
    return list(map(lambda x : x**3,l))    
print("List after function1 " ,func1(l0))

"Function 2. Create a list with even numbers "
def func2(l):
    return list(filter(lambda x: x % 2 == 0, l))  
print("List after function2 " ,func2(func1(l0)))

"Quadratic equation solver"
def quadratic_equation(a,b,c):
    
    Discriminant = b**2 - 4*a*c
    
    if Discriminant < 0 :
        print("There are no roots")
        return 
    
    elif Discriminant == 0 : 
        x=(1/2/a) * (-b)
        print("x = " , x)
        return x
    
    else:
        x1 = (1/2/a) * (-b + (Discriminant**0.5))
        x2 = (1/2/a) * (-b - (Discriminant**0.5))
        print("x1 = " , x1)
        print("x2 = " , x2)
        return x1,x2

a = int(input('Enter the coefficient before x^2: '))
b = int(input('Enter the coefficient before x: '))
c = int(input('Enter the constant value: '))    
quadratic_equation(a,b,c)

"Pascal triangle"
def pascal(n):
    
    print("First %d rows of Pascal triangle : " % n)
    
    #Factorial function for calculating permutations
    def factorial(x):
        
        if x >= 0 :
            
            if x == 1 or x == 0:
                return 1        
            else:
                factor = 1
                for i in range(2, x+1):
                    factor *= i
                return factor
         
        else:
            return "Mistake"  
        
    if n == 1 :
        print([1])
        
    elif n == 2 :
        print(" " + str([1]))
        print([1 , 1])
    
    else:
        print("  "*int(n) +str([1]))
        print("  "*int(n-1) +str([1,1]))
        for j in range(2,n):           
            l0 = [(lambda k : int(factorial(j) / factorial(j-k) / factorial(k)))(k) \
                  for k in range(j+1)]
            print("  "*int(n-j) + str(l0))
    
N = int(input('Enter the number of rows of Pascal triangle: '))
pascal(N)