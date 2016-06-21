# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 18:14:40 2016

@author: dell
"""

import math as ma
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d

class three_bidies:
    def __init__(self,m1,m2,m3,vez0,_z_e0):  
        self.k_j=4*ma.pi**2*m2  
        self.k_e=4*ma.pi**2*m3
        self.k_s=4*ma.pi**2*m1
        
        z_e0=_z_e0
        x_e0,y_e0=0,0.1
        x_j0,y_j0,z_j0=1./2,0,0
        x_s0,y_s0,z_s0=-1./2,0,0
        
        x_center=(m1*x_s0+m2*x_j0+m3*x_e0)/(m1+m2+m3)
        y_center=(m1*y_s0+m2*y_j0+m3*y_e0)/(m1+m2+m3)
        z_center=(m1*z_s0+m2*z_j0+m3*z_e0)/(m1+m2+m3)

        self.xe,self.ye,self.ze=[x_e0-x_center],[y_e0-y_center],[z_e0-z_center]
        self.vex,self.vey,self.vez=[1e-6],[0],[vez0]
        
        self.xj,self.yj,self.zj=[x_j0-x_center],[y_j0-y_center],[z_j0-z_center]
        self.vjx,self.vjy,self.vjz=[0],[2*ma.pi/ma.sqrt(2)],[0]
        
        self.xs,self.ys,self.zs=[x_s0-x_center],[y_s0-y_center],[z_s0-z_center]
        self.vsx,self.vsy,self.vsz=[0],[-2*ma.pi/ma.sqrt(2)],[0]
        
        self.res=[]
        self.rjs=[] 
        self.rej=[]
        
        self.dt=0.0001
        
    def cal(self):
        t=[0]
        while t[-1]<=10:
            resi=((self.xs[-1]-self.xe[-1])**2+(self.ys[-1]-self.ye[-1])**2+(self.zs[-1]-self.ze[-1])**2)**0.5
            rjsi=((self.xs[-1]-self.xj[-1])**2+(self.ys[-1]-self.yj[-1])**2+(self.zs[-1]-self.zj[-1])**2)**0.5
            reji=((self.xe[-1]-self.xj[-1])**2+(self.ye[-1]-self.yj[-1])**2+(self.ze[-1]-self.zj[-1])**2)**0.5

            vexi=self.vex[-1]-self.k_s*(self.xe[-1]-self.xs[-1])/resi**3*self.dt-self.k_j*(self.xe[-1]-self.xj[-1])/reji**3*self.dt
            veyi=self.vey[-1]-self.k_s*(self.ye[-1]-self.ys[-1])/resi**3*self.dt-self.k_j*(self.ye[-1]-self.yj[-1])/reji**3*self.dt
            vezi=self.vez[-1]-self.k_s*(self.ze[-1]-self.zs[-1])/resi**3*self.dt-self.k_j*(self.ze[-1]-self.zj[-1])/reji**3*self.dt
            
            
            vjxi=self.vjx[-1]-self.k_s*(self.xj[-1]-self.xs[-1])/rjsi**3*self.dt-self.k_e*(self.xj[-1]-self.xe[-1])/reji**3*self.dt
            vjyi=self.vjy[-1]-self.k_s*(self.yj[-1]-self.ys[-1])/rjsi**3*self.dt-self.k_e*(self.yj[-1]-self.ye[-1])/reji**3*self.dt
            vjzi=self.vjz[-1]-self.k_s*(self.zj[-1]-self.zs[-1])/rjsi**3*self.dt-self.k_e*(self.zj[-1]-self.ze[-1])/reji**3*self.dt
            
            
            vsxi=self.vsx[-1]-self.k_j*(self.xs[-1]-self.xj[-1])/rjsi**3*self.dt-self.k_e*(self.xs[-1]-self.xe[-1])/resi**3*self.dt
            vsyi=self.vsy[-1]-self.k_j*(self.ys[-1]-self.yj[-1])/rjsi**3*self.dt-self.k_e*(self.ys[-1]-self.ye[-1])/resi**3*self.dt            
            vszi=self.vsz[-1]-self.k_j*(self.zs[-1]-self.zj[-1])/rjsi**3*self.dt-self.k_e*(self.zs[-1]-self.ze[-1])/resi**3*self.dt
            
            xei=self.xe[-1]+vexi*self.dt
            yei=self.ye[-1]+veyi*self.dt
            zei=self.ze[-1]+vezi*self.dt
            xji=self.xj[-1]+vjxi*self.dt
            yji=self.yj[-1]+vjyi*self.dt
            zji=self.zj[-1]+vjzi*self.dt
            xsi=self.xs[-1]+vsxi*self.dt
            ysi=self.ys[-1]+vsyi*self.dt
            zsi=self.zs[-1]+vszi*self.dt
            
            self.vex.append(vexi)
            self.vey.append(veyi)
            self.vez.append(vezi)
            self.vjx.append(vjxi)
            self.vjy.append(vjyi)
            self.vjz.append(vjzi)
            self.vsx.append(vsxi)
            self.vsy.append(vsyi)
            self.vsz.append(vszi)
            
            self.xe.append(xei)
            self.ye.append(yei)
            self.ze.append(zei)
            self.xj.append(xji)
            self.yj.append(yji)
            self.zj.append(zji)
            self.xs.append(xsi)
            self.ys.append(ysi)
            self.zs.append(zsi)
            
            t.append(t[-1]+self.dt)
            
    def pl(self,style1,slogan1,style2,slogan2,style3,slogan3):
        plt.plot(self.xe,self.ye,style1,label=slogan1)
        plt.plot(self.xj,self.yj,style2,label=slogan2)
        plt.plot(self.xs,self.ys,style3,label=slogan3)
        plt.plot([self.xj[0]],[self.yj[0]],'oy',markersize=8)
        plt.plot([self.xs[0]],[self.ys[0]],'or',markersize=8)
        plt.plot([self.xe[0]],[self.ye[0]],'og',markersize=8)
        
    def pl_3d(self,_ax,style1,slogan1,style2,slogan2,style3,slogan3):
        _ax.plot(self.xe,self.ye,self.ze,style1,label=slogan1)
        _ax.plot(self.xj,self.yj,self.zj,style2,label=slogan2)
        _ax.plot(self.xs,self.ys,self.zs,style3,label=slogan3)
        _ax.plot([self.xj[-1]],[self.yj[-1]],[self.zj[-1]],'oy',markersize=8)
        _ax.plot([self.xs[-1]],[self.ys[-1]],[self.zs[-1]],'or',markersize=8)
        _ax.plot([self.xe[-1]],[self.ye[-1]],[self.ze[-1]],'og',markersize=8)
       
    



plt.figure(figsize=(8,8)) 
A=three_bidies(m1=1,m2=1,m3=1,vez0=0,_z_e0=0)
A.cal()
A.pl('g-','m3','y-','m2','r-','m1')
plt.title('Earth and Jupiter orbiting the Sun with the growth rate 1')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()
'''
fig =plt. figure()
ax = fig.add_subplot(111, projection='3d')
A=three_bidies(m1=1,m2=1,m3=0,vez0=0,_z_e0=1e-6)
A.cal()
A.pl_3d(ax,'g-','m3','y-','m2','r-','m1')
plt.title('three-body problem which m3=0')
ax.set_xlabel('x(AU)')
ax.set_ylabel('y(AU)')
ax.set_zlable('z(AU)')
plt.legend()
plt.show()
'''

'''
#-----------木星质量增长变化 ------------------
B=three_bidies(nn=1)
B.cal()
plt.subplot(221)
B.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

C=three_bidies(nn=10)
C.cal()
plt.subplot(222)
C.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()


D=three_bidies(nn=100)
D.cal()
plt.subplot(223)
D.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()


E=three_bidies(nn=1000)
E.cal()
plt.subplot(224)
E.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

plt.show()
'''