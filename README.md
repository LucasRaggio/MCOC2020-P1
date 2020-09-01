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

En la figura anterior se puede observar dos gráficos, (1) Corresponde a la solución real y mediante Odeint de la ecuación diferencial de un oscilador armonico  .  Se puede ver que el comportamiento del oscilador es subamortiguado (Tiende a la posición 0 en el tiempo mediante oscilaciones). Ambos metodos tienen una diferencia del 0,1 %,  increíble. 

Por otro lado, en el gráfico de la derecha se presenta un método de Euler. Este método se mejoro  diviendo un intervalo de tiempo en tiempos mas pequeños (es lo que hace Odeint pero de manera optimizada y con algoritmos Runge -kutta y mejores).

 Nsubdivisiones = 1 (verde, linea punteada), Nsubdivisiones = 10 (rojo, linea punteada) y  Nsubdivisiones = 100 (naranjo, linea punteada).

Se puede ver que para N > 10 la solución del método Euler tiende a la solución real, sin embargo, esto no es siempre así.  Para NN = 1 se encuentra lejos de la solución. 

Tambien se realizo este método para el oscilador armonico simple pero se necesita subdivisiones de mayor tamaño. 

## Entrega5 - Estudio de convergencia y desempeño

## Entrega6 - Entrega inicial de código

## Entrega Final

