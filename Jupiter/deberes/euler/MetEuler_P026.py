import numpy as np
import matplotlib.pyplot as plt
import h5py
import sys

x0 = float(sys.argv[1])
y0 = float(sys.argv[2])
xn = float(sys.argv[3])
n = int(sys.argv[4])

def Euler(n,y0,x0, xn):
    MQ = np.zeros((n, 4))
    h = (xn - 1)/n
    y = np.zeros(n)
    x = np.zeros(n)
    y[0] = y0
    x[0] = x0

    for i in range(0, n-1):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h * ((3*(x[i])) - (2*(y[i])))

    for i in range(0, n):
        MQ[i, 0] = x[i]
        MQ[i, 1] = y[i]
        MQ[i, 2] = xn
        MQ[i, 3] = i  
    return MQ
a = Euler(n, y0, x0, xn)

def create_h5(a):
    hf = h5py.File('P026.h5', 'w')
    hf.create_dataset('euler', data=a)
    hf.close()
    return print("Archivo .h5 CREADO")
crea = create_h5(a)