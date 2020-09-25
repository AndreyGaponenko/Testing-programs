from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np
a=1
def integrand(t, x):
    return np.cos(a*t-x*np.sin(t))
def telegramf(x):
    return quad(integrand, 0, 10, args=(x))[0]
x=np.linspace(0,10,100)
norm=np.vectorize(telegramf)
fig=plt.subplot()
plt.plot(x,norm(x))
