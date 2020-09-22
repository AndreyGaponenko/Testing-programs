from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
a=1
def integrand(t, x):
    return np.cos(a*t-x*np.sin(t))
def expint(x):
    return quad(integrand, 0, np.inf, args=(x))
y=vec_expint = np.vectorize(expint)
fig = plt.subplots()
x=np.linspace(0,4,16)
y=vec_expint(np.arange(0, 4.0, 0.25)).astype(int)
plt.plot(x,y(x))