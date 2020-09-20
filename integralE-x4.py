import scipy as sp
import math as m
import numpy as n
import sympy as sm
def integral(fun,xmin,xmax,n):
    dx=(xmax-xmin)/n
    sum=0
    for i in range(n):
        sum+=fun(xmin+i*dx)
    return sum*dx
b1=integral(lambda x: m.e**(-x**4),0,m.inf,20000)
print(b1)