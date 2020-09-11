# MCOC2020-P1

## Entrega1 - Integración de ecuaciones diferenciales (Lanzamiento de bala) 

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%201/Trayectoria_bala_negro.png?raw=true)



## Entrega2 -  Primeras predicciones con la EDM básica del satélite
###### ⚠️Codigo en carpeta 'Entrega 2'⚠️
###### ⚠️Codigo en carpeta 'Entrega 2'⚠️

Para que el satélite A pueda orbitar alrededor de la tierra sin que ingrese nuevamente a la atmósfera es necesario lanzarlo desde 700 kilómetros de la superficie de la tierra con una velocidad tangencial de 6819.45 m/s  .  Para conocer la posición y velocidad del satélite en función de parámetros iniciales  se utilizo la teoría gravitacional de Newton y la segunda ley de Newton (ley fundamental de la dinámica).

El sistema diferencial planteado para encontrar la posición y velocidad del satélite es la siguiente:

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%202/Imagenes_Readme/Ecuacio%CC%81n.png?raw=true)

¿Cómo se encontró esta velocidad? Para encontrar la velocidad en que el satélite entraba en la atmósfera se realizo un método en el se simulaba la trayectoria del satélite para una velocidad inicial Vy(0) = Vt . Se comenzó con una velocidad de Vt = 10.000  m/s  y se simulo, el resultado fue que para esa velocidad no ingresaba a la atmósfera. Se fue disminuyendo la velocidad en 0.01 m/s  y ensayando   hasta llegar con la solución final. La velocidad mínima para que el satélite no ingrese nuevamente a la atmósfera es de 6819.45 m/s .




A continuación se presenta la figura 1 y 2, las cuales presentan las historias del tiempo en 3 dimensiones y 2 dimensiones para dos órbitas completas, respectivamente.

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%202/Imagenes_Readme/Pos%20.png?raw=true)

Finalmente, se gráfico la distancia al centro de la tierra del satélite vs tiempo. En la siguiente figura la linea celeste representa la distancia del centro de la tierra con el satélite, la linea roja representa a la atmósfera y la café a la tierra. Ademas, se aprecia que para la velocidad mínima justo no alcanza a ingresar a la atmósfera.

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%202/Imagenes_Readme/R(t)%20vs%20T%20.png?raw=true)


## Entrega3 - I/O de vectores de estado y predicciones usando la EDM básica

1658006.2226918892 metros 

## Entrega4 - Implementar una mejora a la EDM


![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%204/Grafico%20E4.png?raw=true)


En la figura anterior se puede observar dos gráficos, (1) Corresponde a la solución real y mediante Odeint de la ecuación diferencial de un oscilador armonico  .  Se puede ver que el comportamiento del oscilador es subamortiguado (Tiende a la posición 0 en el tiempo mediante oscilaciones). Ambos metodos tienen una diferencia del 0,1 %,  increíble. 

Por otro lado, en el gráfico de la derecha se presenta un método de Euler. Este método se mejoro  diviendo un intervalo de tiempo en tiempos mas pequeños (es lo que hace Odeint pero de manera optimizada y con algoritmos Runge -kutta y mejores).

 Nsubdivisiones = 1 (verde, linea punteada), Nsubdivisiones = 10 (rojo, linea punteada) y  Nsubdivisiones = 100 (naranjo, linea punteada).

Se puede ver que para N > 10 la solución del método Euler tiende a la solución real, sin embargo, esto no es siempre así.  Para NN = 1 se encuentra lejos de la solución. 

Tambien se realizo este método para el oscilador armonico simple pero se necesita subdivisiones de mayor tamaño. 

## Entrega5 - Estudio de convergencia y desempeño

###### a)
En la siguiente Grafica se presenta la posición (x,y,z) en el tiempo del vector de estado de Sentinel 1A/B que me tocó. Para esto, descargue y utilice la función leer_eof.py para poder trabajar con los archivos EOF. 

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Pos%20SC.png?raw=true) 

Donde la línea azul es la orbita real (obtenida del archivo EOF) y la naranja es la predicha. Se puede observar que poco a poco la distancia entre la prediccion y ubicacion real aumenta, esto se debe a que para este modelo asumio que la tierra es completamente esferica y la fuerza de gravedad simplificada.  

Para ver en más detalle, el siguiente grafico presenta en términos de la distancia entre satélites medida en el tiempo.


![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Distancia%20SC.png?raw=true) 

El error acumulado por culpa de tener un modelo gravitational inexacto o muy simplificado resulta de alrededor de 2000 km en 24 horas. El tiempo de ejecucion es de 1.488130 Segundos. 


###### b)
Usando la condición inicial (primer OSV) del archivo adjunto en la carpeta 'Entrega 5', se compara la solución entre odeint y eulerint. Se usa Nsubdiviciones=1. A continuacion se grafica la deriva en el tiempo:

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Distancia%20Euler%20Vs%20Odeint--%201%20subdivision.png?raw=true) 

El error por culpa del método inexacto o muy simplificado de Euler Vs Odeint resulta de alrededor de 20000 km en 24 horas. Donde la distancia maxima entre ambas soluciones (prediciones) es de 20881.1 Km. 


###### ¿Cuánto deriva eulerint de odeint en este caso al final del tiempo? 

Deriva entre eulerint y odeint al final del tiempo =  20093.3 Km

###### ¿Cuanto se demora odeint y eulerint respectivamente en producir los resultados?

Tiempo que demora Odeint 0.2956311 Segundos

Tiempo que demora Euler  0.6195548 Segundos


Para ver mayor detalle entre ambos metodos, a continuacion se presenta la pos de la prediccion del satelite en cada caso. 

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Posicion%20Euler%20Vs%20Odeint--%201%20subdivision.png?raw=true) 

###### c)
Para encontrar las subdivisiones para que la predicción con eulerint al final del tiempo esté en menos de un 1% de error en comparación a Odeint, se utilizo un método de aproximación nùmerica. Se realizaron subdivisiones = 10, .... 100, 1000...1500. Para N = 1000, se presento unn error del 26%, un tiempo de ejecución de 566 segundos y una distancia maxima entre ambos satelites de 1136 kilómetros. 

Para una subdivision de N =1500, se obtuvo un tiempo de ejecucion de 825 segundos para el caso de Euler y 0,2 segundos para el caso de Odeint. La distancia Deriva entre Eulerint y Odeint al finnal del tramo es de 758, 4 Km. A continuacion se presenta el grafico de la deriva y la posicion de la prediccion del satelite en cada caso. 

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Euler_VS_Odeint_N1500.png?raw=true) 

El metodo de Odeint es CLARAMENTE superior al método de Euler, esto se debe a que la funcion de Odeint fue elaborada con un codigo de bajo nivel. Ademas, para Euler Int se debe buscar manualmente Subdivisiones para mejorar la solucion. 

Para Buscar el N tal que se cumpla el 1% Se demoraba mucho en ejecutar el programa. 


###### d)

(5pt) Implemente las correcciones J2 y J3. Repita los gráficos de arriba para su caso particular. ¿Cuánta deriva incurre al agregar las correcciones J2 y J3? ¿Cuanto se demora su código en correr?

Anteriormente se analizo la prediccion asumiendo que la tierra es completamente esferica y la fuerza de gravedad simplificada. Ahora corregiremos esos supuestos mediante coeficientes J2(la tierra es una elipsoide achatada) y J3. 



Se presenta la posición (x,y,z) y deriva entre la predicción y lo real en el tiempo del vector de estado de Sentinel 1A/B utilizadno la corrección J2. El tiempo de ejecucion del programa es de: 1.43352465 Segundos. 

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Pos%20CJ2.png?raw=true) 

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Distancia%20J2.png?raw=true) 

Hay una clara mejora respecto a lo analizado en la parte (a). 1945 Km vs 6.4 Km. Impresionante. 


A continucacion se presenta la posición (x,y,z) y deriva entre la predicción en el tiempo del vector de estado de Sentinel 1A/B utilizadno la corrección J3 y J2. El tiempo de ejecucion del programa es de: 1.4531755 Segundos. 


![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Pos%20CJ2%20y%20CJ3.png?raw=true) 

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Distancia%20J2%20y%20J3.png?raw=true) 


Hay una clara mejora respecto a lo analizado en la parte (a). 1945 Km vs 7.9 Km, sin embargo, al añadir la mejora J3 se obtuvo un peor resultado que solo utilizando la correccion J2. ¿Que pasa con J3? Comparemos J3 vs sin correccion. A continuacion se presenta la posición (x,y,z)  y deriva entre la predicción en el tiempo del vector de estado de Sentinel 1A/B utilizadno la corrección J3. El tiempo de ejecucion del programa es de: 1.631755 Segundos. 



![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Dis%20J3%20sol.png?raw=true) 





## Entrega 6 y 7  - ENTREGA FINAL 🇨🇱 CONCURSO MUNDIAL 🌎

Luego de multples analisis y estudios para obtener una buena aproximacion de la posicion del satelite. Se decidio por un codigo que tenga una aproximacion de alrededor de 10 kilometros (o menor) para 24  pero sin disminuir la velocidad de ejecuion del codigo. Por lo tanto, mi apuesta va totalmente por un codigo veloz pero sin tanta precision. 


Para esto SOLO se realizo la correccion J2 (la tierra es una elipsoide achatada). Hay que arriesgarse. 

A continuacion Se presenta la posición (x,y,z) y deriva entre la predicción y lo real en el tiempo del vector de estado de Sentinel 1A/B utilizadno la corrección J2. El tiempo de ejecucion del programa es de: 1.43352465 Segundos. 

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Pos%20CJ2.png?raw=true) 

![alt text](https://github.com/LucasRaggio/MCOC2020-P1/blob/master/Entrega%205/Fotos/Distancia%20J2.png?raw=true) 

Hay una clara mejora respecto al modelo que considera la tierra como una esfera perfecta  1945 Km vs 6.4 Km. Impresionante. 


