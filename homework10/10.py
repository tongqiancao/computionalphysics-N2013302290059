import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
sigma=10
b=8./3

class Lorentz:
    def __init__(self,r=0,dt=0):
        self.vx,self.vy,self.vz=[0],[0],[0]
        self.x,self.y,self.z=[1],[0],[0]
        self.t=[0]
        self.r=r
        self.dt=dt
    def caculate(self):
        i=0
        while self.t[i]<=30:
            self.vx.append(sigma*(self.y[i]-self.x[i]))
            self.vy.append(-self.x[i]*self.z[i]-self.y[i]+self.r*self.x[i])
            self.vz.append(self.x[i]*self.y[i]-b*self.z[i])
            self.x.append(self.x[i]+self.vx[i+1]*self.dt)
            self.y.append(self.y[i]+self.vy[i+1]*self.dt)
            self.z.append(self.z[i]+self.vz[i+1]*self.dt)
            self.t.append(self.t[i]+self.dt)
            i=i+1
    def caculate2(self):
        self.y2=[]
        self.z2=[]
        i=0
        while self.t[i]<=400:
            self.vx.append(sigma*(self.y[i]-self.x[i]))
            self.vy.append(-self.x[i]*self.z[i]-self.y[i]+self.r*self.x[i])
            self.vz.append(self.x[i]*self.y[i]-b*self.z[i])
            self.x.append(self.x[i]+self.vx[i+1]*self.dt)
            self.y.append(self.y[i]+self.vy[i+1]*self.dt)
            self.z.append(self.z[i]+self.vz[i+1]*self.dt)
            self.t.append(self.t[i]+self.dt)
            if self.t[i]>=30:
                if abs(self.x[i])<=1e-3:
                    self.y2.append(self.y[i])
                    self.z2.append(self.z[i])
            i=i+1
            

    def pl(self,style='',slogan=''):
        plt.plot(self.t,self.z,style,label=slogan)
    def pl2(self,style='',slogan=''):
        plt.plot(self.x,self.z,style,label=slogan)    
    def pl3(self,color,slogan):
        plt.scatter(self.y2,self.z2,s=0.3,c=color,label=slogan)
        plt.title('Lorentz modul: z verse y when x=0')
        plt.xlabel('x')
        plt.ylabel('z')
        plt.legend()
        plt.show()
    
'''
png.1
A=Lorentz(r=5,dt=0.0001)
A.caculate()
A.pl(style='',slogan='r=5')
B=Lorentz(r=10,dt=0.0001)
B.caculate()
B.pl(style='',slogan='r=10')
C=Lorentz(r=25,dt=0.0001)
C.caculate()
C.pl(style='',slogan='r=25')
plt.title('Lorentz model z versus time')
plt.xlabel('t')
plt.ylabel('z')
plt.legend()
plt.show()
'''
'''
png.2
C=Lorentz(r=25,dt=0.0001)
C.caculate()
C.pl2(style='k-',slogan='r=25')
plt.title('Lorentz model z versus x')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()
plt.show()
'''
'''
png.3
C=Lorentz(r=25,dt=0.0001)
C.caculate2()
C.pl3(color='k',slogan='r=25')
'''

B=Lorentz(r=160,dt=0.0001)
B.caculate()
B.pl(style='',slogan='r=160')
C=Lorentz(r=160.3,dt=0.0001)
C.caculate()
C.pl(style='',slogan='r=163.8')
plt.title('Lorentz model z versus time')
plt.xlabel('t')
plt.ylabel('z')
plt.legend()
plt.show()


        
