import matplotlib.pyplot as plt
import numpy as np
def act(x):
    return 0 if x<=0 else 1
def go(C):
    x=np.array([C[0],C[1],1])
    w1=[1,1,-1.5]
    w2=[1,1,-0.5]
    w_hidden = np.array([w1,w2])
    w_out = np.array([-1,1,-0.5])
    sum1=np.dot(w_hidden,x)
    print(sum1)
    out=[act(x) for x in sum1]
    print(out)
    out.append(1)
    print(out)
    out=np.array(out)
    print(out)
    sum1=np.dot(w_out,out)
    y=act(sum1)
    return y
C1=[(1,0),(0,1)]
C2=[(0,0),(1,1)]
print(go(C2[0]))