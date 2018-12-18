#Grafica la curva y = x^3 en el intervalo [−10; 10] con 10, 20 y 50 puntos.
import matplotlib.pyplot as plt
import random
import numpy as np

#funcion que grafica,recibe las series y el nombre del archivo a generar
def plot(x, y, vx, vy, graphname):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='pink', linewidth = 2)#rosa las lineas
    ax.scatter(vx, vy, color='purple', marker='o')#morados los puntos
    plt.savefig(graphname)#nombre de gráfica
    plt.show()

def getY(x):
    return pow(x,3)

#serie de 10 puntos
x10 = np.arange(-10, 10, 2.0)# se generan los puntos 
y10=[]
for x in x10:
    y10.append(getY(x)) #se calcula x^3 para c/u

#serie de 20 puntos
x20 = np.arange(-10, 10, 1.0)
y20=[]
for x in x20:
    y20.append(getY(x))

#serie de 100 puntos
x100 = np.arange(-10, 10, 0.4)
y100=[]
for x in x100:
    y100.append(getY(x))

#se manda a graficar cada serie
plot(x10, y10,x10,y10,"graph10.png")
plot(x20, y20,x20,y20,"graph20.png")
plot(x100, y100,x100,y100,"graph100.png")
