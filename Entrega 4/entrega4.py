import scipy as sp
from scipy.integrate import odeint 
import matplotlib.pylab as plt 
from pylab import rcParams
import math 
import numpy as np
import sys 
from pylab import *
import matplotlib.pyplot as plt
from numpy import sin,cos

m = 1.    #kg
f = 1.0
e = 0.2
w = math.pi*2*f # = (k/m - (c/(2*m))**(2))  **0.5
print(w)

k = m *   w**2
c = 2*e*w*m
print (c)


rcParams['figure.figsize'] = 7 , 7

plt.figure(1)

x0 = 1
v0 = 1
z0 = sp.array([ x0 , v0])

#Solucion ODEINT ------------------------------------------------

    
def zp(z , t):
    zp = sp.zeros(2)    
    zp[0] = z[1]        #Z punto[0] es igual a la velocidad en x     
    zp[1] = (-c/m)*z[1] - (k/m)*z[0]           #Z1 es igual a la pos 
            
    return zp


#vector de tiempo 
t =  sp.linspace(0, 10, 100)   # Segundos 


sol = odeint(zp, z0 , t)     #Funcion de (z,t) ; condiciones iniciales; tiempo de la solucion
x = sol[:, 0]
plt.plot(t,x,label = 'z_odeint', linewidth=2, c='c')



#Solucion analitica ------------------------------------------------

y_real = x0 * exp(-c*t/(2*m)) *cos(w*t -0.213003)
plt.plot(t,y_real,label = 'z_real', linewidth=2 , c= 'k')

     
      
#Solucion Euler ------------------------------------------------


plt.grid()
plt.legend()
plt.savefig('Armonico' ,dpi = 300)
plt.show()


















plt.figure(2)

z0 = 1 
t = linspace(0,2,10)
a = 2 


def zp(z,t):
    return a*z


def eulerint(zp, z0,  t, Nsubdivisiones):
    
    Nt = len(t)
    Ndim = len(array([z0]))
    
    z = zeros((Nt, Ndim))
    z[0,:]= z0
    print (z)
    
    for i in range(1, Nt):
        
        t_anterior = t[i-1]     
        dt = (t[i]- t[i-1])/Nsubdivisiones 
        
        z_temp = z[i-1, :].copy()
        print(z_temp, 'Esto es ztemporal')    
        
        for k in range(Nsubdivisiones):                
            z_temp+= dt*zp(z_temp, t_anterior + k*dt)
            
        z[i,:]= z_temp
      
    return z



sub = [1,10,100]
co =  ['g', 'r', 'orange']

for i in range(len(sub)):
    z_euler = eulerint(zp, z0,  t , sub[i])       
    plt.plot(t, z_euler,'--', label= 'z_euler', c = co[i])



plt.grid()
plt.legend()
plt.savefig('Euler' ,dpi = 300)








    