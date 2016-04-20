# this program caculate the velocity of a freely object moving horizontally with a constant velocity,v

from pylab import *

x=[]
t=[]
v=40
t0=0
t_end=float(raw_input('please input the end time:'))
x0=float(raw_input('please input the initial x:'))
dt=float(raw_input('please input the time interval:'))
t.append(t0)
x.append(x0)
for i in range(int(t_end/dt)):
  x.append(x[i]+v*dt)
  i=i+1
  t.append(i*dt)
print t
print x  
plot(t, x, 'bo', color='red', linewidth=1.0, linestyle='--', label='v=v0+gt')
title('x & t')
xlabel('t')
ylabel('x')
legend(loc='upper left')
show()




