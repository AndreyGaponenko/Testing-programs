import numpy as np
def f(x):
    return 2/(1+np.exp(-x))-1
def df(x):
    return 0.5*(x+1)*(1-x)
W1=np.array([[0.2,0.3,0.4,0.5],[0.1,0.15,0.2,0.3]])
W2=np.array([0.4,0.5])
def go_forward(inp):
    sum1=np.dot(W1,inp)
    out=np.array([f(x) for x in sum1])
    sum1=np.dot(W2,out)
    y=f(sum1)
    return(y,out)
def train(epoch):
    global W1,W2
    lmd=0.01
    N=10000
    count=len(epoch)
    for n in range(N):
        x=epoch[np.random.randint(0,count)]
        y,out=go_forward(x[0:4])
        e=y-x[-1]
        delta=e*df(y)
        W2[0]=W2[0]-lmd*delta*out[0]
        W2[1]=W2[1]-lmd*delta*out[1]
        delta2=W2*delta*df(out)
        W1[0,:]=W1[0,:]-lmd*delta2[0]*np.array(x[0:4])
        W1[1,:]=W1[1,:]-lmd*delta2[1]*np.array(x[0:4])
epoch=[(-1,1,-1,1,1),(-1,1,1,1,-1),(-1,-1,-1,1,-1),(1,1,1,1,1),(1,-1,-1,1,1),(1,-1,-1,-1,-1),(1,1,1,-1,-1),(1,-1,1,-1,1)]
train(epoch)
print(W1,W2)
for x in epoch:
    y,out=go_forward(x[0:4])
    print(f"Выходное значение НС: {y}=>{x[-1]}")        

    