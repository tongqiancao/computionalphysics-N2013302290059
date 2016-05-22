import math
import matplotlib.pyplot as plt
class cannon:
  def __init__(self,v0=700,theta=1,dt=0.5):
      self.v0=v0
      self.theta=math.radians(theta)
      self.dt=dt
      self.T=300
      self.a=6.5e-3
      self.g=9.8
      self.bm=1e-4
      self.x=[0]
      self.y=[0]
      self.vx=[self.v0*math.cos(self.theta)]
      self.vy=[self.v0*math.sin(self.theta)]
      self.v=[self.v0]
  def free(self):
      i=0
      while self.y[-1]>=0:
          self.x.append(self.x[i]+self.vx[i]*self.dt)
          self.vx.append(self.vx[i])
          self.y.append(self.y[i]+self.vy[i]*self.dt)
          self.vy.append(self.vy[i]-self.g*self.dt)
          self.v.append(math.sqrt(self.vx[i+1]**2+self.vy[i+1]**2))
          i=i+1
  def  withdrag(self):
      i=0
      while self.y[-1]>=0:
          self.x.append(self.x[i]+self.vx[i]*self.dt)
          self.vx.append(self.vx[i]-self.bm*self.v[i]*self.vx[i]*self.dt)
          self.y.append(self.y[i]+self.vy[i]*self.dt)
          self.vy.append(self.vy[i]-self.g*self.dt-self.bm*self.v[i]*self.vy[i]*self.dt)
          self.v.append(math.sqrt(self.vx[i]**2+self.vy[i]**2))
          i=i+1
        
  def withdensitycorrection(self):
      i=0
      while self.y[-1]>=0:
          self.x.append(self.x[i]+self.vx[i]*self.dt)
          self.y.append(self.y[i]+self.vy[i]*self.dt)
          self.vx.append(self.vx[i]-self.bm*self.v[i]*self.vx[i]*self.dt*(1-self.a*self.y[i]/self.T)**2.5)
          
          self.vy.append(self.vy[i]-self.g*self.dt-self.bm*self.v[i]*self.vy[i]*self.dt*(1-self.a*self.y[i]/self.T)**2.5)
          self.v.append(math.sqrt(self.vx[i]**2+self.vy[i]**2))
          i=i+1


  def pl(self,style='black',slogan=''):
      plt.plot(self.x,self.y,style,label=slogan)
      
class findtrajectory:
    def __init__(self,v0=0,theta=0,dt=0,bm=1e-5,g=9.8,a=6.5e-3,T=300,distance=0):
        self.v0=v0
        self.theta=0
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
        for i in range(90):
            theta=math.radians(i)
            self.vx=[self.v0*math.cos(theta)]
            self.vy=[self.v0*math.sin(theta)]
            j=0
            while self.y[-1]>=0:
                self.x.append(self.x[i]+self.vx[i]*self.dt)
                self.y.append(self.y[i]+self.vy[i]*self.dt)
                self.vx.append(self.vx[i]-self.bm*self.v[i]*self.vx[i]*self.dt*(1-self.a*self.y[i]/self.T)**2.5)
          
                self.vy.append(self.vy[i]-self.g*self.dt-self.bm*self.v[i]*self.vy[i]*self.dt*(1-self.a*self.y[i]/self.T)**2.5)
                self.v.append(math.sqrt(self.vx[i]**2+self.vy[i]**2))
                j=j+1

               
            if self.x[-1]-self.distance>=1000:
                break


    def pl(self,style='',slogan=''):
        plt.plot(self.x,self.y,style,lable=slogan)
      

#A=findtrajectory(distance=6000,dt=0.5)
#A.scaning()
#A.pl(slogan='distance=10000')

A=findtrajectory(distance=10000,dt=0.5)
A.scaning()
A.pl(slogan='distance=10000')


#B=cannon(v0=700,theta=45,dt=0.5)
#B.withdrag()
#B.pl(style='g-',slogan='with drag') 

#for i in range(7):
 #   C=cannon(v0=700,theta=i*15,dt=0.5)
 #   C.withdensitycorrection()
 #   C.pl(style='-',slogan='') 



plt.xlabel('x/m')
plt.ylabel('y/m')
plt.grid()
plt.title('different trajectory ')
plt.legend()
plt.show()   