import math
import matplotlib.pyplot as plt

class baseball:
    def __init__(self,vx0=0,vy0=0,vz0=0,dt=0,omegx=0,omegy=0,omegz=0):
        self.vx0,self.vy0,self.vz0=vx0,vy0,vz0
        self.x,self.y,self.z=[0],[0],[0]
        self.vx,self.vy,self.vz=vx0,vy0,vz0
        self.omegx,self.omegy,self.omegz=omegx,omegy,omegz
        self.dt=dt
        self.v=math.sqrt(vx0**2+vy0**2+vz0**2)
        self.B2m=0.0039+0.0058/(1+math.exp((self.v-35)/5))
        self.S0m=4.1e-4
        self.g=9.8
    def withdrag(self):
        i=0
        while self.y[i]>=0:
            self.x.append(self.x[i]+self.vx*self.dt)
            self.y.append(self.y[i]+self.vy*self.dt)
            self.z.append(self.z[i]+self.vz*self.dt)
            self.vx=-self.B2m*self.v*self.vx*self.dt+self.S0m*self.vy*self.omegz*self.dt+self.vx
            self.vy=-self.g*self.dt-self.B2m*self.v*self.vy*self.dt+self.S0m*self.vz*self.omegx*self.dt+self.vy
            self.vz=-self.B2m*self.v*self.vz*self.dt+self.S0m*self.vx*self.omegy*self.dt+self.vz
            i=i+1
    def pl(self,_a,_vz):             
        _a.plot(self.z, self.x,self.y)
        _a.scatter([self.z[0],self.z[-1]],[self.x[0],self.x[-1]],[self.y[0],self.y[-1]])
        _a.text(self.z[-1], self.x[-1]-80, self.y[-1],'omega_z = %.2f rad/s'%_vz,fontsize=10)
        print 'x=%0.2f'%self.x[-1]

fig= plt.figure(figsize=(6,6))
ax = plt.subplot(1,1,1,projection='3d')
for vz in [0,400]:          
    A=baseball(40,40,0, 0.1,0,200,vz)
    A.withdrag()
    A.pl(ax,vz)
ax.set_xlabel('z (m)')
ax.set_ylabel('x (m)')
ax.set_zlabel('y (m)')
ax.set_title('baseball trajectory')
ax.set_xlim(-100,200)
ax.set_ylim(0,180)
ax.set_zlim(0,100)
plt.show(fig)   






       
        
    

        
