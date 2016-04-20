#this program describe how the number of individuals in a population ,N,varies with time

from pylab import *

N=[]
t=[]   


t0=0
t_end=float(raw_input('please input the end time:'))
N0=float(raw_input('please input the initial N:'))
dt=float(raw_input('please input the time interval:'))
a=float(raw_input('please input the parameter a:'))
b=float(raw_input('please input the parameter b:'))

t.append(t0)
N.append(N0)
for i in range(int(t_end/dt)):
  N.append(N[i]+(a*N[i]-b*(N[i]**2))*dt)
  i=i+1
  t.append(i*dt)
print t
print N  
plot(t, N, 'bo', color='red', linewidth=1.0, linestyle='--', label='dN/dt=aN-bN**2"')
title('N & t')
xlabel('t')
ylabel('N')
legend(loc='upper left')
show()

