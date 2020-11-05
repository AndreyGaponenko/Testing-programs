from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
def holtsmark0(t,u):
    if (u==0):
        z=0
    else:
        z=t*np.sin(t)*np.exp(-(t/u)**(3/2))
    return z
def holtsmark1(u):
    if (holtsmark0==0) and (u==0):
        return 0
    if u!=0:
        return quad(holtsmark0, 0, np.inf, args=(u), limit=10000)[0]*2/(np.pi*u)
holtsmark1_vec=np.vectorize(holtsmark1)
q=4.8e-10 #СГСЭ ед
N=1e15 #см^(-3)
E0=2*np.pi*(4/15)**(2/3)*q*N**(2/3)#СГСЭ ед * см^(-2)
T=1 #эВ
c=3e10 #см/с
m=1.67e-24 #г
V=np.sqrt(2*T/(m*c**2*(0.625e12)))*c
Nue=N**(1/3)*V
a=5.29e-9 #см
h=4.1e-15 #эВ*с
def fun_destribution(E):
    if (E==0) and (holtsmark1_vec==0):
        return 0
    if E!=0:
        return holtsmark1(E/E0)/E0
fun_vec_destribution=np.vectorize(fun_destribution)
def dest_mod1(k,w):
    return quad(lambda E: fun_vec_destribution(E)*(w-3*a*q*E*0.625e12)**k/((Nue*h)**2+(w-3*a*q*E*0.625e12)**2),0,1000,limit=1000)[0]
dest_vec_mod1=np.vectorize(dest_mod1)
def dest_mod2(k,w):
    return quad(lambda E: fun_vec_destribution(E)*(w+3*a*q*E*0.625e12)**k/((Nue*h)**2+(w-3*a*q*E*0.625e12)**2),0,1000,limit=1000)[0]
dest_vec_mod2=np.vectorize(dest_mod2)
def J_dep(k,w):
    return 2*(w)**k/((Nue*h)**2+(w)**2)+dest_vec_mod1(k,w)+dest_vec_mod2(k,w)
def J_abs(w):
    return (J_dep(0,w)*J_dep(2,w)-J_dep(1,w)**2)/(J_dep(2,w)**2+(Nue*h)**2*J_dep(1,w)**2)
w=np.linspace(-1e-3,1e-3,200)
plt.figure(figsize=(14,10))
plt.plot(J_dep(2,w)**2+(Nue*h)**2*J_dep(1,w)**2)