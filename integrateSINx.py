import scipy as sc
import math as m
import numpy as nm
def sq(func, xmin, xmax, n):
    dx = 1.0 * (xmax-xmin) / n
    sum = 0.0
    for i in range(n):
        sum+=func(xmin+i*dx)
    return sum*dx
b1 = sq(lambda x: nm.sin(x),0,m.pi,200)
print(b1)
