import scipy as sp
from scipy import integrate
y=lambda x: sp.e**(-x**4)
z=integrate.quad(y,0,sp.inf)[0]
print(z)
