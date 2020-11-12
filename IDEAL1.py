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
def E0(N):
    return 2*np.pi*(4/15)**(2/3)*q*N**(2/3)#СГСЭ ед * см^(-2)
c=3e10 #см/с
m=1.67e-24 #г
def Nue(N,T):
    return N**(1/3)*np.sqrt(2*T/(m*c**2*(0.625e12)))*c
a=5.29e-9 #см
h=4.1e-15 #эВ*с
def fun_destribution(E,N):
    if (E==0) and (holtsmark1_vec==0):
        return 0
    if E!=0:
        return holtsmark1(E/E0(N))/E0(N)
fun_vec_destribution=np.vectorize(fun_destribution)
def dest_mod1(k,w,N,T):
    return quad(lambda E: fun_vec_destribution(E,N)*(w-3*a*q*E*0.625e12)**k/((Nue(N,T)*h)**2+(w-3*a*q*E*0.625e12)**2),0,1000,limit=1000)[0]
dest_vec_mod1=np.vectorize(dest_mod1)
def dest_mod2(k,w,N,T):
    return quad(lambda E: fun_vec_destribution(E,N)*(w+3*a*q*E*0.625e12)**k/((Nue(N,T)*h)**2+(w-3*a*q*E*0.625e12)**2),0,1000,limit=1000)[0]
dest_vec_mod2=np.vectorize(dest_mod2)
def J_dep(k,w,N,T):
    return 2*(w)**k/((Nue(N,T)*h)**2+(w)**2)+dest_vec_mod1(k,w,N,T)+dest_vec_mod2(k,w,N,T)
def J_abs(w,N,T):
    return (J_dep(0,w,N,T)*J_dep(2,w,N,T)-J_dep(1,w,N,T)**2)/(J_dep(2,w,N,T)**2+(Nue(N,T)*h)**2*J_dep(1,w,N,T)**2)
w=np.linspace(-1e-3,1e-3,100)
plt.figure(figsize=(14,10))
plt.plot(w,J_abs(w,1e16,1),color="red", label="N=10^16 см^(-3) и Т=1 эВ")
plt.plot(w,J_abs(w,1e17,1),color="blue", label="N=10^17 см^(-3) и Т=1 эВ")
plt.plot(w,J_abs(w,1e18,1),color="green", label="N=10^18 см^(-3) и Т=1 эВ")
plt.title("Распределение интенсивности с учётом движения ионов")
plt.xlabel("Сдвиг частоты,эВ")
plt.legend()
