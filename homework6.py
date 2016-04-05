#this program describe the trajectory of our cannon shell including both air drag ang the reduced air density at high altitudes 
#coding:utf-8
from pylab import *
import math

x=[]
v_x=[]
y=[]
v_y=[]
t=[]
   
t0=0
x0=0
y0=0
i=0
v=float(raw_input('please input the initial v:'))
theta=float(raw_input('please input the initial angle:'))
dt=float(raw_input('please input the time interval:'))
T0=float(raw_input('please input the parameter T0:'))
B=float(raw_input('please input the parameter B:'))
m=float(raw_input('please input the parameter m:'))
g=float(raw_input('please input the parameter g:'))

v_x0=math.cos(theta)
v_y0=math.sin(theta)

t.append(t0)
x.append(x0)
v_x.append(v_x0)
y.append(y0)
v_y.append(v_y0)
while not(t!=0 and y==0):
  x.append(x[i]+v_x[i]*dt)
  v_x.append(v_x[i]-(B/m)*((1-6.5e-3*y[i]/T0)**2.5)*dt)
  y.append(y[i]+v_y[i]*dt)
  v_y.append(v_y[i]-((B/m)*((1-6.5e-3*y[i]/T0)**2.5)+g)*dt)
  i=i+1
  t.append(i*dt)  

print x
print y  
plot(x, y, 'bo', color='red', linewidth=1.0, linestyle='--', label='cannon trajectory')
title('x & t')
xlabel('x')
ylabel('y')
legend(loc='upper left')
show()

