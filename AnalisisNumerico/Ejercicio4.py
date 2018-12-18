import matplotlib.pyplot as plt
import random
import numpy as np

def coeff(vx, vy):
    a = vy.copy()
    m = len(vx)
    for k in range(1, m):
        for i in range(k, m):
            a[i] =(a[i] - a[k-1]) / (vx[i] - vx[k-1])
    return a


def evalPoly(a, vx, x):
    n = len(vx) -1
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x - vx[n-k])*p
    return p

def plot(x, y, vx, vy):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='pink', linewidth = 2)
    ax.scatter(vx, vy, color='purple', marker='o')
    plt.savefig('newton.png')
    plt.show()

vx = [-4,-4,-3,-2,-1,0,1,2,3,4,5]
vy = [0,0,0.05,0.25,0.75,1,.75,.25,.05,0,0]
a = coeff(vx, vy)
for x in vx:
    print(evalPoly(a, vx, x))

#seriex = np.arange(-5, 5, .1)
#seriey = []
#for x in seriex:
#    seriey.append(evalPoly(a, vx, x))

#plot(seriex, seriey, vx, vy)