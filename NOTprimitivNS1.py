import numpy as np
def f(x):
    return 2/(1+np.exp(-x))-1
def df(x):
    return 0.5*(1+x)*(1-x)
W1=np.array([[-0.2,0.3,-0.4], [0.1,-0.3,-0.4]])
W2=np.array([0.2,0.3])
def go_forward(inp):
    sum1=np.dot(W1,inp)
    out=np.array([f(x) for x in sum1])
    sum1=np.dot(W2,out)
    y=f(sum1)
    return(y,out)
def train(epoch):
    global W2,W1
    lmd=0.01 #шаг обучения
    N=10000 #Число итераций при обучении
    count=len(epoch)
    for k in range(N):
        x=epoch[np.random.randint(0,count)] #Случайный выбор входного сигнала из обучающей выборки
        y,out=go_forward(x[0:3]) #Прямой проход по НС и вычисление выходных значений нейронов
        e=y-x[-1] #Ошибка
        delta=e*df(y) #Локальный градиент
        W2[0]=W2[0]-lmd*delta*out[0]
        W2[1]=W2[1]-lmd*delta*out[1] #Корректировка веса первой и второй группы
        delta2=W2*delta*df(out) #Вектор из 2 величин локальных градиентов
        #Корректировка связей первого слоя
        W1[0,:]=W1[0,:]-np.array(x[0:3])*delta2[0]*lmd
        W1[1,:]=W1[1,:]-np.array(x[0:3])*delta2[1]*lmd
epoch=[(-1,-1,-1,-1),(-1,-1,1,1),(-1,1,-1,-1),(-1,1,1,1),(1,-1,-1,-1),(1,-1,1,1),(1,1,-1,-1),(1,1,1,-1)] 
train(epoch)
for x in epoch:
    y,out=go_forward(x[0:3])
    print(f"Выходное значение НС: {y}=>{x[-1]}")
       