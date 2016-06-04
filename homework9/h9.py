# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 15:32:31 2016

@author: dell
"""

import math
import matplotlib.pyplot as plt
pi=math.pi

class ocillatory:
    def __init__(self,OmegaD=0,FD=0,dt=0):
        self.t=[0]
        self.omega=[0]
        self.OmegaD=OmegaD
        self.dt=dt
        self.gl=1
        self.theta=[0]
        self.q=0.5
        self.FD=FD
    def forcedpendulum(self,color,solgan):
        i=0
        self.newtheta=[0]
        self.newomega=[0]
        while self.t[i]<=500:
            self.omegai=self.omega[i]-self.gl*math.sin(self.theta[i])*self.dt-self.q*self.omega[i]*self.dt+self.FD*math.sin(self.OmegaD*self.t[i])*self.dt
            self.thetai=self.theta[i]+self.omegai*self.dt
            self.t.append(self.t[i]+self.dt)
            if self.thetai>=pi:self.thetai-=2*pi
            if self.thetai<=-pi:self.thetai+=2*pi
            self.theta.append(self.thetai)
            self.omega.append(self.omegai)
            if abs(math.sin(4*self.OmegaD*self.t[i]))<=1e-7:
                self.newtheta.append(self.thetai)
                self.newomega.append(self.omegai)
            i=i+1
        plt.scatter(self.newtheta,self.newomega,s=0.5,c=color,label=solgan)



c=ocillatory(OmegaD=2./3,FD=0,dt=0.01*pi)
c.forcedpendulum('red','fd=0')
       
plt.title('forced pendulum')
plt.xlabel('$\theta$ /rad')
plt.ylabel('$\omega$ /rad/s')
plt.legend()
plt.show()
        