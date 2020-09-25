import scipy as sp
from scipy.stats import hypergeom
import math
from math import factorial
import numpy as np
def psi(n1,n1s,m,n,ns):
    return hypergeom.pmf(-n1,-n1s,m+1,-4*n*ns/((n-ns)**2))
print(psi(-1,-2,1,2,-0.25))
def gen( ns, n1s, n2s, m, n, n1, n2, a):
    return (((-1)**(n1s+n2s))*(a/(4*(factorial(m))**2))*math.sqrt(factorial(n1+m)*factorial(n2+m)*factorial(n1s+m)*factorial(n2s+m)/(factorial(n1)*factorial(n1s)*factorial(n2)*factorial(n2s)))*((4*n*n1s/((n-n1s)**2))**(m+2))*(((n-ns)/(n+ns))**(n+ns)))
print(gen(1,1,1,0,2,1,2,1))
def gen2(ns,n1s,n2s,m,n,n1,n2):
    return (2*(n1s-n2s)*((n**2+ns**2)/(n+ns)**3)-(n1-n2)*(4*n*n1/(n+ns)**2))*psi(n1,n1s,m,n,ns)*psi(n2,n2s,m,n,ns)-2*((n1s*psi(n1,n1s-1,m,n,ns))*psi(n2,n2s,m,n,ns)-n2s*psi(n1,n1s,m,n,ns)*psi(n2,n2s-1,m,n,ns))
print(gen2(1,1,1,0,2,1,2))
def final(ns,n1s,n2s,m,n,n1,n2,a):
    return gen(ns,n1s,n2s,m,n,n1,n2,a)*gen2(ns,n1s,n2s,m,n,n1,n2)
