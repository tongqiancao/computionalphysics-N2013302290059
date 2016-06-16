# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:21:20 2016

@author: dell
"""
 
import matplotlib.pyplot as plt
import math
pi=math.pi

class doublestar:
    def __init__(self,m1,m2,dt):
        self.x1,self.y1=[1./3],[0]
        self.m1=m1
        self.m2=m2
        self.dt=dt
        self.x20=2./3
        self.x2,self.y2=[-self.x20],[0]
        self.vx1,self.vy1=[0],[2*pi/math.sqrt(3)]
        self.vx2,self.vy2=[0],[-4*pi/math.sqrt(3)]
        self.t=[0]
    def caculate(self):
        i=0
        while self.t[i]<=2:
            self.r=math.sqrt((self.x1[i]-self.x2[i])**2+(self.y1[i]-self.y2[i])**2)
            self.a=4*math.pi**2/self.r**3
            self.vx1.append(self.vx1[i]-self.a*self.m2*(self.x1[i]-self.x2[i])*self.dt)
            self.x1.append(self.x1[i]+self.vx1[i+1]*self.dt)
            self.vy1.append(self.vy1[i]-self.a*self.m2*(self.y1[i]-self.y2[i])*self.dt)
            self.y1.append(self.y1[i]+self.vy1[i+1]*self.dt)
            self.vx2.append(self.vx2[i]-self.a*self.m1*(self.x2[i]-self.x1[i])*self.dt)
            self.x2.append(self.x2[i]+self.vx2[i+1]*self.dt)
            self.vy2.append(self.vy2[i]-self.a*self.m1*(self.y2[i]-self.y1[i])*self.dt)
            self.y2.append(self.y2[i]+self.vy2[i+1]*self.dt)
            self.t.append(self.t[i]+self.dt)
            i=i+1
    def pl(self,style):
        plt.plot(self.x1,self.y1,style)
        plt.plot(self.x2,self.y2,style)
        plt.plot([self.x1[-1]],[self.y1[-1]],'ob',markersize=10)
        plt.plot([self.x2[-1]],[self.y2[-1]],'og',markersize=10)
        
A=doublestar(2,1,0.001)
A.caculate() 
A.pl(style='')
plt.xlabel('x/AU') 
plt.ylabel('y/AU')
plt.title('the trajectory when m1/m2=2')
plt.legend()  
plt.show()    