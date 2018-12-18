#Has una gr´afica con 100 puntos que intente replicar la siguiente
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5) #random con semilla en 5
x = np.arange(1, 101) #100 puntos desde 1 hasta 101, para no incluir el cero
#Generamos la y con una distribución normal
#desv. estandar de 50 para que se vea el efecto de arriba y abajo
y = (3 * x) + np.random.normal(0, 50, 100) 
colors = np.random.rand(100) #100 colores random para los puntos
area = np.pi * (15 * np.random.rand(100))**2 # ranfom de 0 a 15 puntos para el radio de c/punto
#gráfic de scatter con los parámetros antes calculados + opacidad
plt.scatter(x, y,s=area, c=colors, alpha=0.5)
#abrir la graf.
plt.show()