from scipy.special import hyp2f1
import math
from math import factorial
def psi(ni,nis,ms,n,ns):
    return hyp2f1(-ni,-nis,ms,-4*n*ns/((n-ns)**2))
def gen(n,n1,n2,m,ns,n1s,n2s,a):
    return (((-1)**(n1s+n2s))*(a/(4*(factorial(abs(m-1)))**2))*math.sqrt(factorial(n1+m)*factorial(n2+m)*factorial(n1s+abs(m-1))*factorial(n2s+abs(m-1))/(factorial(n1)*factorial(n1s)*factorial(n2)*factorial(n2s)))*((4*n*ns/((n-ns)**2))**(m+1))*(((n-ns)/(n+ns))**(n+ns)))
def gen2(n,n1,n2,m,ns,n1s,n2s):
    return psi(n1,n1s,m,n,ns)*psi(n2,n2s,m,n,ns)-(((n-ns)/(n+ns))**2)*psi(n1+1,n1s,m,n,ns)*psi(n2+1,n2s,m,n,ns)
def final(n,n1,n2,m,ns,n1s,n2s,a):
    return gen(n,n1,n2,m,ns,n1s,n2s,a)*gen2(n,n1,n2,m,ns,n1s,n2s)
print(final(3,0,0,2,2,0,0,1)**2)
print(final(3,1,1,0,2,0,0,1)**2)
print(final(3,1,0,1,2,1,0,1)**2)
print(final(3,1,0,1,2,0,1,1)**2)
print(final(3,2,0,0,2,0,0,1)**2)