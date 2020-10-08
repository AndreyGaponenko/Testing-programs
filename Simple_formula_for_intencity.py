import math
def simple_intencity(n,n1,n2,m,ns,n1s,n2s,ms,a):
    b=math.sqrt(4*n*ns/(n-ns)**2)
    if ((n1==n1s) and (n2==n2s) and (ms==m-1)):
        xMm=(a/4)*b*math.sqrt((n1+m)*(n2+m))*(1-(n1+1)*(n2+1)/b**2)
        print(xMm**2)
    if ((n1==n1s+1) and (n2==n2s+1) and (ms==m+1)):
        xmM=(a/4)*b*math.sqrt(n1*n2)*(1-(m+n1)*(m+n2)/b**2)
        print(xmM**2)
    if ((n1==n1s+1) and (n2==n2s) and (ms==m)):
        z_positiv_k=(a/4)*b*math.sqrt((n1+m)*n1)
        print(z_positiv_k**2)
    if ((n1==n1s) and (n2==n2s+1) and (ms==m)):
        z_negativ_k=(a/4)*b*math.sqrt((n2+m)*n2)
        print(z_negativ_k**2)
simple_intencity(3,1,1,0,2,1,0,0,1)
simple_intencity(3,1,1,0,2,0,1,0,1)
simple_intencity(3,1,0,1,2,0,0,1,1)
simple_intencity(3,2,0,0,2,1,0,0,1)
print('Перпендикулярная поляризованность:')
simple_intencity(3,0,0,2,2,0,0,1,1)
simple_intencity(3,1,1,0,2,0,0,1,1)
simple_intencity(3,1,0,1,2,1,0,0,1)
simple_intencity(3,1,0,1,2,0,1,0,1)






        
    