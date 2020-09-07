import scipy as sp
from scipy.integrate import odeint 
import matplotlib.pylab as plt 
from pylab import rcParams
import math 
import numpy as np
import sys 
from pylab import *
import matplotlib.pyplot as plt
from leer_eof import utc2time, leer_eof
from time import perf_counter 

#Unidades 
km = 1000 #metros 
G = 6.674 * 10**(-11)   # Nm2/kg2
w = 7.292115 * 10 **(-5)        #rad/s

# DATOS 

Rt = 6371*km                  #Radio de la tierra 
x0 = 700*km
Mt = 5.972 * 10**(24)         #kg 
J2= 1.75553 * 10**10  * km**5  # m^5 /s^2
J3 = -2.61913 * 10**11 * km**6  # m^6 /s^2

t = 0
cc = math.cos(w*t)
ss = math.sin(w*t)

R = np.array([[ cc , --ss, 0 ],
              [ ss ,  cc, 0  ],
              [  0 ,  0 ,  1 ]])
Rp=  np.array([[ -ss , -cc, 0 ],
               [cc ,  -ss, 0  ],
               [ 0 , 0  ,  0  ]] )* w 
Rp2 =  np.array([[ -cc , ss,0],
                 [-ss , -cc,0 ],
                 [  0 ,0 ,  0 ]] )* w*w 

RT  = R.T


#Funcion a integrar

# z es el vector de estado 
# z = [x, y, z,  vx, vy , vz]
# df/dt = Satelite(z,t)
    
    #       = [   z2   ] 
    # df/dt = [        ] 
    #       = [   z2p  ]  

#Vector de estado 
# z[0]  - > x 
# z[1]  - > y
# z[2]  - > z

# z[3]  - > vx 
# z[4]  - > vy 
# z[5]  - > vz

correccion = 0

#------------Funcion Pro --------------------
    
def satelite(z , t):
    zp = sp.zeros(6)     
    zp[0] = z[3]    #Z punto[0] es igual a la velocidad en x 
    zp[1] = z[4]    #Z punto[1] es igual a la velocidad en y     
    zp[2] = z[5]    #Z punto[2] es igual a la velocidad en z 
    
    z1 = z[0:3]                   # Deja las primeras 3 componentes  (posicion en sus componentes) eje inercial
    r2 = sp.dot(z1,z1)
    r  = sp.sqrt((r2))           # Distancia desde el eje de la tierra al satelite
   
    v = z[3:6]                   # Saca las primeras 3 componentes quedando la velocidad en sus componentes 

        
    c1 = 398600.440*km**3/(r**3)
    c2 = 2* (RT @ Rp)
    c3 = RT@Rp2
    
    z2p = -c1*z1 - ( c2@v  + c3@z1 )
    
    xs = z1[0]
    ys = z1[1]
    zs = z1[2]
    
    rflat = (xs**2. + ys**2.)
    
    FJ2 = zeros(3)    
    FJ2[0] = J2 * (xs/r**7.) * ( 6. * zs**2 - 1.5*rflat)
    FJ2[1] = J2 * (ys/r**7.) * ( 6. * zs**2 - 1.5*rflat)
    FJ2[2] = J2 * (zs/r**7.) * ( 3. * zs**2 - 4.5*rflat)    
    FJ2_convert = RT@FJ2


    FJ3 = zeros(3)    
    FJ3[0] = J3 * (xs*zs/r**9.) * ( 10. * zs**2 - 7.5*rflat)
    FJ3[1] = J3 * (ys*zs/r**9.) * ( 10. * zs**2 - 7.5*rflat)
    FJ3[2] = J3 * (1/r**9.) * ( 4. * zs**2 *(zs**2 - 3.*rflat) +1.5*rflat**2)
    FJ3_convert = RT@FJ3    
    
    if correccion == 0:    
        zp[3] =  z2p[0] 
        zp[4] =  z2p[1] 
        zp[5] =  z2p[2] 
        
    if correccion == 1: 
        zp[3] =  z2p[0] + FJ2_convert[0]
        zp[4] =  z2p[1] + FJ2_convert[1]
        zp[5] =  z2p[2] + FJ2_convert[2]
        
    if correccion == 2: 
        zp[3] =  z2p[0] + FJ2_convert[0] + FJ3_convert[0]
        zp[4] =  z2p[1] + FJ2_convert[1] + FJ3_convert[1]
        zp[5] =  z2p[2] + FJ2_convert[2] + FJ3_convert[2]  
    
    
    return zp


def eulerint(satelite,z0,t,Nsubdivisiones):
    
    Nt = len(t)
    Ndim = len(sp.array(z0))
    z = zeros((Nt,Ndim))
    z[0,:] = z0
    
    for i in range(1,Nt):
        t_anterior = t[i-1]
        dt = (t[i] - t[i-1])/float(Nsubdivisiones)
        z_temp = z[i-1,:].copy()
        for k in range(Nsubdivisiones):
            z_temp +=  dt * satelite(z_temp, t_anterior+k*dt)
        z[i,:] = z_temp  
    return z


#------------------------------------------------

eof = leer_eof("fname")

tiempo  = eof[0]
eof_x   = eof[1]
eof_y   = eof[2]
eof_z   = eof[3]
eof_Vx  = eof[4]
eof_Vy  = eof[5]
eof_Vz  = eof[6]


x_i = eof_x[0]    #metros 
y_i = eof_y[0]    #metros 
z_i = eof_z[0]  #metros 
vx_i = eof_Vx[0] # m/s 
vy_i = eof_Vy[0]
vz_i = eof_Vz[0] # m/s


datos = (len(eof_x) -1)
Delta_t= (tiempo[len(tiempo) -1 ])  -  (tiempo[0]) 


#vector de tiempo 
t =  sp.linspace(0, Delta_t , datos+1)   # Segundos 


#-----------Condiciones iniciales --------------
z0 = sp.array([ x_i , y_i, z_i , vx_i , vy_i, vz_i ])
#------------------------------------------------


t1 = perf_counter() 
sol = odeint(satelite, z0 , t)     #Funcion de (z,t) ; condiciones iniciales; tiempo de la solucion
t2 = perf_counter() 
x = sol[:, 0]
y = sol[:, 1]
z = sol[:, 2]



Nsubdivisiones = 1500

t3 = perf_counter() 
sol_euler = eulerint(satelite, z0 , t,Nsubdivisiones)
t4 = perf_counter() 
Euler_x = sol_euler[:, 0]
Euler_y = sol_euler[:, 1]
Euler_z = sol_euler[:, 2]
    

x_H = [ 0 , 5*60*60, 10*60*60, 15*60*60 , 20*60*60, 25*60*60]
x_H_text = [ '0' , '5','10' , '15','20' , '25']

y_Km = [ -5000000 ,0, 5000000]
y_Km_text = [ '-5000' , '0','5000']




rcParams['figure.figsize'] = 8 , 6


plt.subplot(3,1,1)
plt.title("Euler Vs Odeint Sub = 1500 )", fontweight = 'bold') 
plt.ylabel ('X (KM)' , fontweight = 'bold')
plt.plot(t, Euler_x  , c='c')
plt.plot(t, x , c= 'orange')

plt.xticks( x_H, x_H_text, rotation = 90 )
plt.yticks( y_Km, y_Km_text)



plt.subplot(3,1,2)
plt.ylabel ('Y (KM)' , fontweight = 'bold')
plt.plot(t, Euler_y , c = 'c')
plt.plot(t, y,  c= 'orange')
plt.xticks( x_H, x_H_text, rotation = 90 )
plt.yticks( y_Km, y_Km_text)



plt.subplot(3,1,3)
plt.ylabel ('Z (KM)' , fontweight = 'bold')
plt.xlabel ('Tiempo, t (Horas)',  fontweight = 'bold' )
plt.plot(t, Euler_z ,c= 'c')
plt.plot(t, z,  c= 'orange')
plt.xticks( x_H, x_H_text, rotation = 90 )
plt.yticks( y_Km, y_Km_text)
plt.savefig('Posicion Euler Vs Odeint-- 1500 subdivision' ,dpi = 300)
plt.show()
dis = 0

# --------------------------------------

def distancia(x,y,z, x1,y1,z1):
    rs = [] 
    
    for i in range(datos):
        ri = 0
        rt = 0 
        xi = x[i]
        yi = y[i]
        zi = z[i]
        
        rt = ((xi)**2 + (yi)**2 + (zi)**2)**0.5
        
        x1i = x1[i]
        y1i = y1[i]
        z1i = z1[i]        
        ri = (  (xi-x1i)**2 + (yi-y1i)**2 + (zi-z1i)**2)**0.5
        rs.append(ri)
        
        print (ri/rt)


    return array(rs)


t =  sp.linspace(0, Delta_t , datos)   # Segundos 


plt.figure(3)
r_Euler_Odeint = distancia(x,y,z,Euler_x ,Euler_y ,Euler_z)  

D_max = round(max(r_Euler_Odeint)/1000,1)
plt.plot(t,r_Euler_Odeint/1000 )

titulo = 'Euler vs Odeint -- 1500 subdivision, D_max =', D_max, 'Km'
plt.title( titulo , fontweight = 'bold') 
plt.ylabel ('Deriva (KM)' , fontweight = 'bold')
plt.xlabel ('Tiempo, t (Horas)',  fontweight = 'bold' )
plt.xticks( x_H, x_H_text, rotation = 90 )
plt.savefig('Distancia Euler Vs Odeint-- 1500 subdivision' ,dpi = 300)
plt.show()



print ('Deriva entre eulerint y odeint al final del tiempo = ',round(r_Euler_Odeint[datos-1]/1000,1) ,'Km')
print ('Tiempo que demora Odeint', round((t2 - t1),7) ,'Segundos')
print ('Tiempo que demora Euler ', round((t4 - t3),7), 'Segundos')


