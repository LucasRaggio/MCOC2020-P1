import scipy as sp
from scipy.integrate import odeint 
import matplotlib.pylab as plt 
from pylab import rcParams


#Unidades 
cm = 0.01 # m 
inch = 2.54*cm


#Parametros 
p = 1.225               # kg/m*3
cd = 0.47 
D= 8.5*inch
r = D/2 
A = sp.pi * (r**2)      # Area tranversal de la bala
g = 9.81                # m/s**2
m = 15.                 # kg 
CD = 0.5 * p * cd * A   # Coeficiente de arrastre. 




#Funcion a integrar

# z es el vector de estado 
# z = [x, y , vx, vy]
# dz/dt = bala (z,t)
    
    #       = [   z2   ] 
    # dz/dt = [        ]
    #       = [FD/m - g]


#Vector de estado 
# z[0]  - > x 
# z[1]  - > y
# z[2]  - > vx 
# z[3]  - > vy 
rcParams['figure.figsize'] = 7 , 5
    
def bala(z , t):
    zp = sp.zeros(4)
    zp[0] = z[2]    #Z punto es igual a la velocidad en x 
    zp[1] = z[3]    #Z punto es igual a la velocidad en y 
    v = z[2:4]   # Saca las ultimas dos componentes 
    
    v2 = sp.dot(v,v)
    vnorm = sp.sqrt(v2)    #dot = producto punto
    FD = - CD * v2 * (v / vnorm)   
    v[0] = v[0] - V
    
    zp[2] = FD[0] / m 
    zp[3] = FD[1] / m - g 
    
    return zp


#vector de tiempo 



vi = 100*1000./3600.


t = sp.linspace(0, 6 , 1001)    
z0 = sp.array([ 0 , 0 , vi  ,vi ])

Vi = [0, 10, 20]
Vi_text = ['V=0 m/s', 'V=10.0 m/s', 'V=20.0 m/s']




plt.figure(1)
for n in range(len(Vi)): 
    V = Vi[n]
    sol = odeint(bala, z0 , t)     #Funcion de (z,t) ; condiciones iniciales; tiempo de la solucion
    x = sol[:, 0]
    y = sol[:, 1]
    plt.plot(x,y, label = Vi_text[n])


plt.grid() 
plt.ylim([0,50])
plt.xlim([0,150])
plt.ylabel ('Y (m)' , fontweight = 'bold')
plt.xlabel ('X (m)',  fontweight = 'bold' )
plt.title("Trayectoria para distintos vientos", fontweight = 'bold') 

plt.tight_layout()  
plt.legend()
plt.savefig('Trayectoria_bala' ,dpi = 300)
plt.show()
#--------------------------------

  




