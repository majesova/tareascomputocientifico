#Has una gr´afica de tipo scatter que tome una distribuci´on normal estandar tanto en X como en Y, con 200 puntos
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import random
import numpy as np

# funcion que grafica,recibe las series y el nombre del archivo a generar
def plot(x, y, vx, vy, graphname):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='blue', linewidth = 1)#rosa las lineas
    ax.scatter(vx, vy, color='red', marker='*') #morados los puntos
    plt.savefig(graphname) #nombre de gráfica
    plt.show()

mu, sigma = 0, 0.1 # media y desviación estándar
start = mu - 5 * sigma #Desde -5
stop = mu + 5 * sigma #Hasta +5
x = np.linspace(start, stop , 200) #Genera 200 valores con el inicio y fin que se asignaron previamente
y = mlab.normpdf(x, mu, sigma) #Retorna la "normal probability density" con media de mu y desviacion estándar mu evaluando los valores de x
plot(x,y,x,y,"scattergaussian.png")


