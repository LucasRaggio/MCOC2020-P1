import scipy as sp
from scipy.integrate import odeint 
# import matplotlib.pylab as plt 
# from pylab import rcParams
import math 
import numpy as np
import sys 
# from pylab import *
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




rrs =[]
Tierra_a_satelite =[]



#------------Funcion Pro --------------------
    
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

        
    c1 = G*Mt/(r**3)
    c2 = 2* (RT @ Rp)
    c3 = RT@Rp2
    
    z2p = -c1*z1 - ( c2@v  + c3@z1 )
    
    zp[3] =  z2p[0]
    zp[4] =  z2p[1]
    zp[5] =  z2p[2]
    
    return zp

#------------------------------------------------



import datetime as dt 

 # <List_of_OSVs count="9361">


      # <X unit="m">299061.452952</X>
      # <Y unit="m">2504739.190677</Y>
      # <Z unit="m">-6617606.990132</Z>
      # <VX unit="m/s">2395.743301</VX>
      # <VY unit="m/s">-6748.728991</VY>
      # <VZ unit="m/s">-2447.219878</VZ>
      # <TAI>TAI=2020-07-25T23:00:19.000000</TAI>
      # <UTC>UTC=2020-07-25T22:59:42.000000</UTC>
      # <UT1>UT1=2020-07-25T22:59:41.787032</UT1>
      # <Absolute_Orbit>+33617</Absolute_Orbit>
x_i = 299061.452952     #metros 
y_i = 2504739.190677    #metros 
z_i = -6617606.990132   #metros 
vx_i = 2395.743301 # m/s 
vy_i=  -6748.728991 # m/s
vz_i=  -2447.219878 # m/s


      # <TAI>TAI=2020-07-27T01:00:19.000000</TAI>
      # <UTC>UTC=2020-07-27T00:59:42.000000</UTC>
      # <UT1>UT1=2020-07-27T00:59:41.787584</UT1>
      # <Absolute_Orbit>+33633</Absolute_Orbit>
      # <X unit="m">1758481.857868</X>
      # <Y unit="m">6851700.745053</Y>
      # <Z unit="m">205527.869685</Z>
      # <VX unit="m/s">1589.991471</VX>
      # <VY unit="m/s">-175.785352</VY>
      # <VZ unit="m/s">-7426.986520</VZ>
      # <Quality>NOMINAL</Quality>

x_f  =   1758481.857868
y_f  =   6851700.745053
z_f  =   205527.869685
vx_f =   1589.991471
vz_f =   -175.785352
vz_f =   -7426.986520



utc_EOF_format =        "%Y-%m-%dT%H:%M:%S.%f"
# t1 = dt.datetime.strptime("2020-07-25T22:59:42.000000",utc_EOF_format)
# t2 = dt.datetime.strptime("2020-07-27T00:59:42.000000",utc_EOF_format)
t1 = dt.datetime.strptime("2018-08-14T22:59:42.000000",utc_EOF_format)
t2 = dt.datetime.strptime("2018-08-16T00:59:42.000000",utc_EOF_format)

intervalo = t2 -t1 
intervalor_en_segundos = intervalo.total_seconds()








#vector de tiempo 
t =  sp.linspace(0, intervalor_en_segundos , 1000)   # Segundos 


#-----------Condiciones iniciales --------------
z0 = sp.array([ x_i , y_i, z_i , vx_i , vy_i, vz_i ])
#------------------------------------------------



sol = odeint(satelite, z0 , t)     #Funcion de (z,t) ; condiciones iniciales; tiempo de la solucion
x = sol[:, 0]
y = sol[:, 1]
z = sol[:, 2]
    




# Pos final estimadas
x_f= (x[-1])
y_f= (y[-1])
z_f= (z[-1])

dvec = (x_f - x_i)**2 + (y_f - y_f)**2 +  (z_f- z_f)**2

dd = sp.sqrt((dvec))


'''                                 ---

     -          -       -      -     -        
    -  -      -    -    -      -     -
   - - - -   -      -   -      -     -
  -       -   -    -    -      -     -
 -         -    - -     - - - -      -     '''
     

print ('')
print ('')
print ('')
print ('La distanica entre la posición real y la estimada es:', dd )
print ('')
print ('')
print ('')




















































# # ----------Grafico 3D Tierra con Orbita -----------

# rcParams['figure.figsize'] = 7 , 7
# fig = plt.figure(1)
# ax = plt.axes(projection='3d')



# Atmosfera = Rt + 80*km

# # Hago la Tierra en 3D
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0,  np.pi, 100)
# cx = []
# cy = []
# cz = []
# cx2= []
# cy2= []
# for i in u: 
#     for j in v:
#         cx.append(Rt*math.cos(i)* math.sin(j))
#         cy.append(Rt*math.sin(i)* math.sin(j))  
#         cz.append(Rt *math.cos(j))
#         cx2.append((Rt+80000)*math.cos(i))
#         cy2.append((Rt+80000)*math.sin(i))   





# ax.plot3D(x, y, z, 'c' , label ='Orbita')
# plt.plot( x_i, y_i, z_i , 'o', c= 'red')
# plt.plot( [0,0], [0,Atmosfera], '-', c='k')
# plt.plot( [0,0], [0,-Atmosfera], '-', c='k')
# plt.plot( [0,Atmosfera], [0,0], '-', c='k')
# plt.plot( [0,-Atmosfera], [0,0], '-', c='k')
# ax.plot3D(cx, cy, cz, 'peru' , alpha = 0.2, label = 'Tierra')  
# plt.plot( cx2 , cy2 , c = 'salmon' , label = 'Atmosfera')      #Atmosfera
  
# plt.grid() 

# plt.ylabel ('Y (m)' , fontweight = 'bold')
# plt.xlabel ('X (m)',  fontweight = 'bold' )
# plt.title("Satelite A", fontweight = 'bold') 
# plt.ticklabel_format(useOffset = False, style = 'plain')

# plt.tight_layout()  
# plt.legend()
# plt.savefig('Satelite 3D' ,dpi = 300)
# plt.show()


# # ----------Grafico 2D Tierra, Orbita y Atmosfera -----------


# fig = plt.figure(2)
# Atmosfera = Rt + 80*km


# # Hago la Tierra en 2D
# cx = []
# cy = []

# for i in u: 
#     for j in v:
#         cx.append(Rt*math.cos(i))
#         cy.append(Rt*math.sin(i))
       
        

# plt.plot(x,y, c='c', label ='Orbita')                   #Orbita Satelite
# plt.plot( cx  ,  cy , c = 'peru' , label = 'Tierra')      #Tierra 
# plt.plot( cx2 , cy2 , c = 'salmon' , label = 'Atmosfera')      #Atmosfera
# plt.plot( [0,0], [0,Atmosfera], '--', c='k')
# plt.plot( [0,0], [0,-Atmosfera], '--', c='k')
# plt.plot( [0,Atmosfera], [0,0], '--', c='k')
# plt.plot( [0,-Atmosfera], [0,0], '--', c='k')


# plt.grid() 

# plt.ylabel ('Y (m)' , fontweight = 'bold')
# plt.xlabel ('X (m)',  fontweight = 'bold' )
# plt.title("Satelite A 2D", fontweight = 'bold') 
# plt.ticklabel_format(useOffset = False, style = 'plain')

# plt.tight_layout()  
# plt.legend()
# plt.savefig('Satelite 2D' ,dpi = 300)
# plt.show()





# # ----------Grafico Distancia Tierra vs satelite -----------

# rcParams['figure.figsize'] = 5 , 8

# plt.figure(3)



# t =  sp.linspace(0, 11890 , len(Tierra_a_satelite))   # Segundos 

# plt.plot( t , Tierra_a_satelite , '--' , c='c' , label = 'Pos Sate')
# plt.axhline( y = 80000 + Rt, c='salmon' , linewidth=3 ,label = 'Atmosfera')
# plt.axhline( y =  Rt, c='peru' , linewidth=3 ,label = 'Tierra')

# plt.grid() 
# plt.ticklabel_format(useOffset = False, style = 'plain')
# plt.ylabel ('Distancia (m)' , fontweight = 'bold')
# plt.xlabel ('T (t)',  fontweight = 'bold' )
# plt.title("Distancia centro tierra a satelite", fontweight = 'bold') 
# plt.tight_layout()  
# plt.legend(loc= 'upper left', bbox_to_anchor=[0,1],fancybox=True)
# plt.savefig('Distancia_centro_tierra_a_satelite' ,dpi = 300)
# plt.show()









