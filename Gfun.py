from mpmath import mp, fp
import math
from sympy import *
import sympy as sp
from math import factorial
def gamar(a,n):
    return (math.gamma(a+n)/math.gamma(a))
def geom(a,b,c,z):
    n=0
    p=0
    f=gamar(a,n)*gamar(b,n)*(z**n)/(gamar(c,n)*factorial(n)
    while (f > 0.00001):
        for n in sp.inf:
            f=gamar(a,n)*gamar(b,n)*(z**n)/(gamar(c,n)*factorial(n)
            p+=f   
        else:
            f=0
    return p
print(geom(1,1,1,1))