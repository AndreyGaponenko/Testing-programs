import matplotlib.pyplot as plt
import numpy as np
N=5
b=4
x1=np.random.random(N)
x2=x1+[np.random.randint(10)/10 for i in range(N)]+b
C1=[x1,x2]
x1=np.random.random(N)
x2=x1-[np.random.randint(10)/10 for i in range(N)]-0.1+b
C2=[x1,x2]
print(C2)
f=[0+b,1+b]
w2=0.5
w=np.array([-w2,w2,-w2*b])
for i in range (N):
    x=np.array([C1[0][i], C1[1][i], 1])
    y=np.dot(w,x)
    print(x)
    if y>=0:
        print("Класс С1")
    else:
        print("Класс С2")
plt.scatter(C1[0][:], C1[1][:], s=10, c='red')
plt.scatter(C2[0][:], C2[1][:], s=10, c='blue')
plt.plot(f)
plt.grid(True)
plt.show()