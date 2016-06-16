import matplotlib.pyplot as plt
import math
pi=math.pi

class threestar:
    def __init__(self,m1,m2,m3,dt):
        self.x1,self.y1=[0],[0]
        self.xj=5.2
        self.yj=0
        self.xe=1
        self.yj=0
        self.xc=(m2*self.xj+m3*self.xe)/(m2+m3)
        self.x20=self.xe-self.xc
        self.x30=self.xj-self.xc
        self.x2,self.y2=[self.x20],[0]
        self.x3,self.y3=[self.x30],[0]
        self.vx1,self.vy1=[0],[-m2*2*pi-m3*2*pi/math.sqrt(5.2)]        
        self.vx2,self.vy2=[0],[2*pi]
        self.vx3,self.vy3=[0],[2*pi/math.sqrt(5.2)]
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.dt=dt
        self.t=[0]
    def caculate(self):
        i=0
        while self.t[i]<=2:
            self.r12=math.sqrt((self.x1[i]-self.x2[i])**2+(self.y1[i]-self.y2[i])**2)
            self.r23=math.sqrt((self.x2[i]-self.x3[i])**2+(self.y2[i]-self.y3[i])**2)
            self.r13=math.sqrt((self.x1[i]-self.x3[i])**2+(self.y1[i]-self.y3[i])**2)
            self.a12=4*math.pi**2/self.r12**3
            self.a23=4*math.pi**2/self.r23**3
            self.a13=4*math.pi**2/self.r13**3
            self.vx1.append(self.vx1[i]-self.a12*self.m2*(self.x1[i]-self.x2[i])*self.dt-self.a13*self.m3*(self.x1[i]-self.x3[i])*self.dt)
            self.x1.append(self.x1[i]+self.vx1[i+1]*self.dt)
            self.vy1.append(self.vy1[i]-self.a12*self.m2*(self.y1[i]-self.y2[i])*self.dt-self.a13*self.m3*(self.y1[i]-self.y3[i])*self.dt)
            self.y1.append(self.y1[i]+self.vy1[i+1]*self.dt)
            self.vx2.append(self.vx2[i]-self.a12*self.m1*(self.x2[i]-self.x1[i])*self.dt-self.a23*self.m3*(self.x2[i]-self.x3[i])*self.dt)
            self.x2.append(self.x2[i]+self.vx2[i+1]*self.dt)
            self.vy2.append(self.vy2[i]-self.a12*self.m1*(self.y2[i]-self.y1[i])*self.dt-self.a23*self.m3*(self.y2[i]-self.y3[i])*self.dt)
            self.y2.append(self.y2[i]+self.vy2[i+1]*self.dt)
            self.vx3.append(self.vx3[i]-self.a13*self.m1*(self.x3[i]-self.x1[i])*self.dt-self.a23*self.m2*(self.x3[i]-self.x2[i])*self.dt)
            self.x3.append(self.x3[i]+self.vx3[i+1]*self.dt)
            self.vy3.append(self.vy3[i]-self.a13*self.m1*(self.y3[i]-self.y1[i])*self.dt-self.a23*self.m2*(self.y3[i]-self.y2[i])*self.dt)
            self.y3.append(self.y3[i]+self.vy3[i+1]*self.dt)
            self.t.append(self.t[i]+self.dt)
            i=i+1
    def pl(self,style):
        plt.plot(self.x1,self.y1,style)
        plt.plot(self.x2,self.y2,style)
        plt.plot(self.x3,self.y3,style)
        plt.plot([self.x3[-1]],[self.y3[-1]],'oy',markersize=10)
        plt.plot([self.x1[-1]],[self.y1[-1]],'or',markersize=20)
        plt.plot([self.x2[-1]],[self.y2[-1]],'og',markersize=8)
        
A=threestar(2000,1.9,6e-3,0.001)
A.caculate() 
A.pl(style='')
plt.xlabel('x/AU') 
plt.ylabel('y/AU')
plt.title('the trajectory when m1:m2:m3=2000:1.9:6e-3')
plt.legend()  
plt.show() 
'''
A=three_bidies(nn=1)
A.cal()
A.pl('g-','Earth','y-','Jupiter','r-','Sun')
plt.title('m1:m2:m3=2000：1.9：6e-3')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()
'''
'''
B=three_bidies(nn=10)
B.cal()
B.pl('g-','Earth','y-','Jupiter','r-','Sun')
plt.title('m1:m2:m3=2000：19：6e-3')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()

C=three_bidies(nn=100)
C.cal()
C.pl('g-','Earth','y-','Jupiter','r-','Sun')
plt.title('m1:m2:m3=2000：190：6e-3')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()

D=three_bidies(nn=1000)
D.cal()
D.pl('g-','Earth','y-','Jupiter','r-','Sun')
plt.title('m1:m2:m3=2000：1900：6e-3')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()

E=three_bidies(nn=100,theta_e=30)
E.cal()
E.pl('g-','Earth','y-','Jupiter','r-','Sun')
plt.title('m1:m2:m3=2000：1900：6e-3')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()
'''
'''
F=three_bidies(nn=100,theta_e=60)
F.cal()
F.pl('g-','Earth','y-','Jupiter','r-','Sun')
plt.title('m1:m2:m3=2000：19000：6e-3')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()
'''   