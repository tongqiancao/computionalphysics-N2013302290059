# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 15:29:08 2016

@author: dell
"""
import math
import matplotlib.pyplot as plt

class ocillatory:
    def __init__(self,q=0,OmegaD=0,FD=0,dt=0):
        self.t=[0]
        self.omega=[0]
        self.OmegaD=OmegaD
        self.dt=dt
        self.gl=9.8
        self.theta=[0.2]
        self.q=q
        self.FD=FD
    def pendulum(self):
        i=0
        while self.t[i]<=10:
            self.omega.append(self.omega[i]-self.gl*self.theta[i]*self.dt)
            self.theta.append(self.theta[i]+self.omega[i+1]*self.dt)
            self.t.append(self.t[i]+self.dt)
            i=i+1
    def forcedpendulum(self):
        i=0
        while self.t[i]<=15:
            self.omega.append(self.omega[i]-self.gl*self.theta[i]*self.dt-self.q*self.omega[i]*self.dt+self.FD*math.sin(self.OmegaD*self.t[i])*self.dt)
            self.theta.append(self.theta[i]+self.omega[i+1]*self.dt)
            self.t.append(self.t[i]+self.dt)
            i=i+1
    def pl(self,style='',slogan=''):
        plt.plot(self.t,self.theta,style,label=slogan)


A=ocillatory(1,OmegaD=2,FD=0,dt=0.04)
A.forcedpendulum()
A.pl(slogan='FD=0')

B=ocillatory(1,OmegaD=2,FD=0.2,dt=0.04)
B.forcedpendulum()
B.pl(slogan='FD=0.2')

c=ocillatory(1,OmegaD=2,FD=1,dt=0.04)
c.forcedpendulum()
c.pl(slogan='FD=1')
       
plt.title('forced pendulum')
plt.xlabel('t/s')
plt.ylabel('$\theta$/rad')
plt.legend()
plt.show()
        
        
    
            
            
        
        
        