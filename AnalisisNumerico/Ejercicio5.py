import matplotlib.pyplot as plt
import random
import numpy as np
import math

def incrementalSearching(f, a, b, dx, tolerance=None, max_iterations=None):
    """
    :param f: función que se va a evaluar
    :param a: extremo izquierdo del intervalo
    :param b: extremo derecho del intervalo
    :param dx: El valor que se va incrementar
    :return: intervalo a,b
    """
    n = 0 #Se inicializa la primera iteración
    intervalo = []
    while b > a: #mientras no llegue a b sigue iterando
        c = a + dx # incremento de a en la proporción delta
        fc = f(c) # se evalúa la función con c
        a = c #Se reemplaza a para el siguiente paso
        n += 1
        if (tolerance is None) & (max_iterations is None):
            try: #raiz negativa causa una excepción, se aprovecha el lenguaje para saber si puede o no sacarla
                math.sqrt(fc) #Se intenta obtener la raiz de la función
                intervalo.append(c) # se almacena el valor válido
            except:
                pass
        else:
            try: #raiz negativa causa una excepción, se aprovecha el lenguaje para saber si puede o no sacarla
                if(tolerance < fc) & (n < max_iterations):#Si no es menor el # de it y está dentro de la tolerancia evalúa
                    math.sqrt(fc) #Se intenta obtener la raiz de la función    
                    intervalo.append(c) # se almacena el valor válido
                else:
                    return min(intervalo), max(intervalo), n   
            except:
                pass
    if(len(intervalo)>1):#si logró tener el rango debe tener 2
        return min(intervalo), max(intervalo), n #se sacan los máximos y mínimos obtenido de los valores que si pudo
    else:
        return None, None, n


y = lambda x: x**3 - 10*(x**2) + 5 #se define una lambda llamada "y" que permite realizar las sustiticiones de x y ser pasado como una función
#inciso a
minimun, maximum, iterations = incrementalSearching (y, -5., 5., 0.001) #Se llama a la función, 0,0 es que no tiene tolerancia ni max de iteraciones
print("a) [{0},{1}] in {2} iterations".format(minimun, maximum,iterations)) #impresión inciso a
#inciso b
minimun, maximum, iterations = incrementalSearching (y, -5., 5., 0.001,2,20000) #Se llama a la función con 3 de tolerancia y 2000 de 
print("b) [{0},{1}] in {2} iterations".format(minimun, maximum, iterations)) #impresión inciso b

