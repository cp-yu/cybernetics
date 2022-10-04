# 4th
# page 14
from scipy.integrate import  odeint
from numpy import zeros,sin,pi
import matplotlib.pyplot as plt

def PlantModel(y,t,u):
    J=0.0067
    B=0.1
    theta,omega=y
    dydt=[omega,-(B/J)*omega+(1/J)*u]
    return dydt

def main():
    ts=0.001
    xk=zeros(2)
    e1=0
    u1=0
    time=[i*ts for i in range(2000)]
    r=[0.5*sin(2*pi*i*ts) for i in range(2000)]
    y=[0 for _ in range(2000)]
    e=[0 for _ in range(2000)]
    de=[0 for _ in range(2000)]
    u=[0 for _ in range(2000)]

    for k in range(2000):
        para=u1
        tSpan=[0,ts]
        tmp=odeint(PlantModel,xk,tSpan,args=(para,))
        xk=tmp[-1]
        y[k]=xk[0]

        e[k]=r[k]-y[k]
        de[k]=(e[k]-e1)/ts

        u[k]=20*e[k]+0.5*de[k]
        if u[k]>10:u[k]=10
        if u[k]<-10:u[k]=-10

        u1=u[k]
        e1=e[k]
    plt.figure(1)
    plt.plot(time,r,"b",label="r")
    plt.plot(time,y,"g",label="g")
    plt.xlabel("time(s)")
    plt.ylabel("r,y")
    plt.legend("Ideal position signal,\n Position tracking")
    plt.show()
    plt.figure(2)
    temp=[r[i]-y[i] for i in range(2000)]
    plt.plot(time,temp,"r")
    plt.show()




if __name__=="__main__":
    main()