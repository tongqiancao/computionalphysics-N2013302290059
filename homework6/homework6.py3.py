import matplotlib.pyplot as plt
import math


      
class findtrajectory:
    def __init__(self,v0=0,theta=0,dt=0,bm=1e-5,g=9.8,a=6.5e-3,T=300,distance=0):
        self.v0=v0
        self.theta=self.theta=math.radians(45)
        self.dt=dt
        self.T=300
        self.a=6.5e-3
        self.g=9.8
        self.bm=1e-4
        self.distance=distance
        self.x=[0]
        self.y=[0]
        self.v=[v0]
        

      
    def scaning(self):
        self.v0=0
        while self.v0<700:
            self.x=[0]
            self.y=[0]
            self.vx=[self.v0*math.cos(self.theta)]
            self.vy=[self.v0*math.sin(self.theta)]
            i=0
            while self.y[-1]>=0:
                self.x.append(self.x[i]+self.vx[i]*self.dt)
                self.y.append(self.y[i]+self.vy[i]*self.dt)
                self.vx.append(self.vx[i]-self.bm*self.v[i]*self.vx[i]*self.dt*(1-self.a*self.y[i]/self.T)**2.5)
          
                self.vy.append(self.vy[i]-self.g*self.dt-self.bm*self.v[i]*self.vy[i]*self.dt*(1-self.a*self.y[i]/self.T)**2.5)
                self.v.append(math.sqrt(self.vx[i]**2+self.vy[i]**2))
                i=i+1
            
            if abs(self.x[-1]-self.distance)<=10:
                print 'THE aimming velocity of the distance %f is %f'%(self.distance,self.v0)
                print 'the error is %f'%(abs(self.x[-1]-self.distance))
                break
            self.v0= self.v0+0.5
    def pl(self,style='',slogan=''):
        plt.plot(self.x,self.y,style,label=slogan)
 
A=findtrajectory(distance=800,dt=0.01)
A.scaning()
A.pl(slogan='distance=800')

B=findtrajectory(distance=5000,dt=0.01)
B.scaning()
B.pl(slogan='distance=8000')

C=findtrajectory(distance=8000,dt=0.01)
C.scaning()
C.pl(slogan='distance=5000')




plt.xlabel('x/m')
plt.ylabel('y/m')
plt.grid()
plt.title('different trajectory ')
plt.legend()
plt.show()   



