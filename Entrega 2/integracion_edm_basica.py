import scipy as sp
from scipy.integrate import odeint 
import matplotlib.pylab as plt 
from pylab import rcParams
import math 
import numpy as np
import sys 
from pylab import *
import matplotlib.pyplot as plt


# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt


#Unidades 

km = 1000 #metros 
G = 6.674 * 10**(-11)   # Nm2/kg2
w = 7.2722 * 10 **(-5)        #rad/s

# DATOS 

Rt = 6371*km                 #Radio de la tierra 
x0 = 700*km
Mt = 5.972 * 10**(24)       #kg 

t = 0

D = (Rt + x0)

R = np.array([[ math.cos(w*t) , -math.sin(w*t), 0 ],
     [ math.sin(w*t) ,  math.cos(w*t), 0 ],
     [   0     ,   0    ,  1 ]])


Rp=  np.array([[ -math.sin(w*t) , -math.cos(w*t), 0 ],
                 [  math.cos(w*t) ,  -math.sin(w*t), 0 ],
                 [   0     ,   0    ,  0 ]] )* w 


Rp2 =  np.array([[ -math.cos(w*t) ,  math.sin(w*t), 0 ],
                 [  -math.sin(w*t) , -math.cos(w*t), 0 ],
                 [   0     ,   0    ,  0 ]] )* w*w 

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



rcParams['figure.figsize'] = 7 , 7

rrs =[]
Tierra_a_satelite =[]
    
def satelite(z , t):
    zp = sp.zeros(6)
    
    
    zp[0] = z[3]    #Z punto[0] es igual a la velocidad en x 
    zp[1] = z[4]    #Z punto[1] es igual a la velocidad en y     
    zp[2] = z[5]    #Z punto[2] es igual a la velocidad en z 
    
    z1 = z[0:3]                   # Deja las primeras 3 componentes  (posicion en sus componentes) eje inercial
    r2 = sp.dot(z1,z1)
    r  = sp.sqrt((r2))           # Distancia desde el eje de la tierra al satelite
    
    Tierra_a_satelite.append(r)
    rrs.append(((r-Rt)/1000))
    
    if  ((r-Rt)/1000) < 80:
        print ('STOP')
        sys.exit()
   
    v = z[3:6]                   # Saca las primeras 3 componentes quedando la velocidad en sus componentes 
    print (sp.sqrt(sp.dot(v,v)))
        
    c1 = G*Mt/(r**3)
    c2 = 2* (RT @ Rp)
    c3 = RT@Rp2
    
    z2p = -c1*z1 - ( c2@v  + c3@z1 )
    
    zp[3] =  z2p[0]
    zp[4] =  z2p[1]
    zp[5] =  z2p[2]
    
    return zp


#vector de tiempo 
t =  sp.linspace(0, 11890 , 741)   # Segundos 

z0 = sp.array([ D , 0, 0 , 0 , 6819.45 , 0 ])
sol = odeint(satelite, z0 , t)     #Funcion de (z,t) ; condiciones iniciales; tiempo de la solucion
x = sol[:, 0]
y = sol[:, 1]
z = sol[:, 2]
    



# ----------Grafico 3D Tierra con Orbita -----------

fig = plt.figure(1)
ax = plt.axes(projection='3d')



Atmosfera = Rt + 80*km

# Hago la Tierra en 3D
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0,  np.pi, 100)
cx = []
cy = []
cz = []
cx2= []
cy2= []
for i in u: 
    for j in v:
        cx.append(Rt*math.cos(i)* math.sin(j))
        cy.append(Rt*math.sin(i)* math.sin(j))  
        cz.append(Rt *math.cos(j))
        cx2.append((Rt+80000)*math.cos(i))
        cy2.append((Rt+80000)*math.sin(i))   





ax.plot3D(x, y, z, 'c' , label ='Orbita')
plt.plot( [0,0], [0,Atmosfera], '-', c='k')
plt.plot( [0,0], [0,-Atmosfera], '-', c='k')
plt.plot( [0,Atmosfera], [0,0], '-', c='k')
plt.plot( [0,-Atmosfera], [0,0], '-', c='k')
ax.plot3D(cx, cy, cz, 'peru' , alpha = 0.2, label = 'Tierra')  
plt.plot( cx2 , cy2 , c = 'salmon' , label = 'Atmosfera')      #Atmosfera
  
plt.grid() 

plt.ylabel ('Y (m)' , fontweight = 'bold')
plt.xlabel ('X (m)',  fontweight = 'bold' )
plt.title("Satelite A", fontweight = 'bold') 
plt.ticklabel_format(useOffset = False, style = 'plain')

plt.tight_layout()  
plt.legend()
plt.savefig('Satelite 3D' ,dpi = 300)
plt.show()


# ----------Grafico 2D Tierra, Orbita y Atmosfera -----------


fig = plt.figure(2)
Atmosfera = Rt + 80*km


# Hago la Tierra en 2D
cx = []
cy = []

for i in u: 
    for j in v:
        cx.append(Rt*math.cos(i))
        cy.append(Rt*math.sin(i))
       
        

plt.plot(x,y, c='c', label ='Orbita')                   #Orbita Satelite
plt.plot( cx  ,  cy , c = 'peru' , label = 'Tierra')      #Tierra 
plt.plot( cx2 , cy2 , c = 'salmon' , label = 'Atmosfera')      #Atmosfera
plt.plot( [0,0], [0,Atmosfera], '--', c='k')
plt.plot( [0,0], [0,-Atmosfera], '--', c='k')
plt.plot( [0,Atmosfera], [0,0], '--', c='k')
plt.plot( [0,-Atmosfera], [0,0], '--', c='k')


plt.grid() 

plt.ylabel ('Y (m)' , fontweight = 'bold')
plt.xlabel ('X (m)',  fontweight = 'bold' )
plt.title("Satelite A 2D", fontweight = 'bold') 
plt.ticklabel_format(useOffset = False, style = 'plain')

plt.tight_layout()  
plt.legend()
plt.savefig('Satelite 2D' ,dpi = 300)
plt.show()





# ----------Grafico Distancia Tierra vs satelite -----------

rcParams['figure.figsize'] = 5 , 8

plt.figure(3)

plt.plot( t , Tierra_a_satelite , '--' , c='c' , label = 'Pos Sate')
plt.axhline( y = 80000 + Rt, c='salmon' , linewidth=3 ,label = 'Atmosfera')
plt.axhline( y =  Rt, c='peru' , linewidth=3 ,label = 'Tierra')

plt.grid() 
plt.ticklabel_format(useOffset = False, style = 'plain')
plt.ylabel ('Distancia (m)' , fontweight = 'bold')
plt.xlabel ('T (t)',  fontweight = 'bold' )
plt.title("Distancia centro tierra a satelite", fontweight = 'bold') 
plt.tight_layout()  
plt.legend(loc= 'upper left', bbox_to_anchor=[0,1],fancybox=True)
plt.savefig('Distancia_centro_tierra_a_satelite' ,dpi = 300)
plt.show()

print (rrs)

