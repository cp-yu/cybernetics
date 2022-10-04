import matplotlib.pyplot as plt
from control.matlab import *

m=250.0
k=40.0
b=60.0

A= [[0,1],[-k/m,-b/m]]
B=[[0],[1/m]]
C=[[1,0]]
sys=ss(A,B,C,0)

plt.figure(1)
yout,T=step(sys)
plt.plot(T.T,yout.T)
plt.show()

