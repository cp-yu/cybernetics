from control.matlab import  *
import numpy as np
import  matplotlib.pyplot as plt
def main():
    ts=0.001
    sys=tf(5.235e5,[1,87.35,1.047e4,0])
    dsys=c2d(sys,ts,"zoh")
    num,den=tfdata(dsys)
    num=num[0][0]
    den=den[0][0]

    u1,u2,u3=0,0,0
    y1,y2,y3=0,0,0
    x=np.array([[0.,0.,0.]]).T

    error1=0
    time=[k*ts for k in range(500)]
    u=[0 for _ in range(500)]
    y=[0 for _ in range(500)]
    error=[0 for _ in range(500)]
    S=1
    if S==1:
        kp=0.5
        ki=0.001
        kd=0.001
        r=[1 for _ in range(500)]
    elif S==2:
        kp = 0.5
        ki = 0.001
        kd = 0.001
        r=[np.sign(np.sin(4*np.pi*k*ts)) for k in range(500)]
    elif S==3:
        kp = 1.5
        ki = 1.0
        kd = 0.01
        r = [np.sin(4 * np.pi * k * ts)*0.5 for k in range(500)]

    # kp=0
    # kd=0
    # ki=0.1
    for k in range(500):


        y[k]=-den[1]*y1-den[2]*y2-den[3]*y3+num[0]*u1+num[1]*u2+num[2]*u3# Look At Here！
        if k==8:

            print("bad")

        error[k]=r[k]-y[k]
        # if error[k]>5:error[k]=5
        # if error[k]<-5:error[k]=-5

        x[0] = error[k]
        x[1] = (error[k] - error1) / ts
        x[2] = x[2] + error[k] * ts

        u[k] = kp * x[0] + kd * x[1] + ki * x[2]
        if u[k] > 10: u[k] = 10
        if u[k] < -10: u[k] = -10

        u3,u2,u1=u2,u1,u[k]
        y3,y2,y1=y2,y1,y[k]



        error1=error[k]

    plt.plot(time,r,"r")
    plt.plot(time,y,"b")
    plt.xlabel("time(s)")
    plt.ylabel("r,y")
    plt.show()


if __name__=="__main__":
    main()