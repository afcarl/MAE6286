from math import *
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.8                 #Gravitational acceleration
v_t = 30.0              #Trim velocity
C_D = 1/40.             #Drag Coefficient
C_L = 1.                #Lift Coefficient

# Initial Conditions
v0 = v_t                #Initially at trim velocity
theta0 = 0.             #Initial trajectory
x0 = 0.                 #Horizontal start point
y0 = 1000.              #Initial altitude

def f(u):               #Creates system of equations u'(t)=f(u)
    v = u[0]
    theta = u[1]
    x = u[2]
    y = u[3]
    return np.array([-g*np.sin(theta)-(C_D/C_L)*(g/v_t**2)*v**2,
                     -(g/v)*np.cos(theta)+(g/v_t**2)*v,
                     v*np.cos(theta),
                     v*np.sin(theta)])
                     
def euler_step(u,f,dt):
    return u + dt*f(u)

T = 100                  #Final time
dt = input('Enter time step: ')
N = int(T/dt) + 1        #Number of time steps
t = np.linspace(0.0,T,N)

u = np.empty((N,4))                   #Empty matrix of N columns and 4 rows for system of equation
u[0] = np.array([v0,theta0,x0,y0])    #First column is initial conditions

for n in range(N-1):                 #This will populate empty u vector!
    u[n+1] = euler_step(u[n],f,dt)    #Euler method performed using previous value to estimate next

#Recall our stored values for position
x = u[:,2]
y = u[:,3]

#Plot position over time
plt.figure(figsize=(8,6))
plt.grid(True)
plt.xlabel(r'x',fontsize=18)
plt.ylabel(r'y',fontsize=18)
plt.plot(x,y,'k-')
plt.title('Glider Trajectory, Flight Time = %.2f' %T,fontsize=18)

'''print u[:,2]
print u[:,3]'''

plt.show()