import numpy as np
import matplotlib.pyplot as plt
import h5py
import sys

x0 = float(sys.argv[1])
y0 = float(sys.argv[2])
xn = float(sys.argv[3])
n = int(sys.argv[4])

#y0 = float(ay0)
#x0 = float(ax0)
#n = int(an)
#xn= int(axn)

def Euler(n,y0,x0, xn):
    MQ = np.zeros((n, 4))
    h = (xn - 1)/n
    y = np.zeros(n)
    x = np.zeros(n)
    y[0] = y0
    x[0] = x0
    for i in range(0, n-1):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*((3*(x[i])) - (2*(y[i])))
    for i in range(0, n):
        MQ[i, 0] = x[i]
        MQ[i, 1] = y[i]
        MQ[i, 2] = xn
        MQ[i, 3] = i 
        print(i)
    return MQ
a = Euler(n, y0, x0, xn)
print(a)
def create_h5(a):
    hf = h5py.File('test2.h5', 'w')
    hf.create_dataset('euler', data=a)
    hf.close()
    return print("Archivo .h5 CREADO")

crea = create_h5(a)
def read_h5():
    fh = h5py.File('./test2.h5', 'r')
    data = fh.get('euler').value
    return print(data)
n = int(input("Escriba UNO leer H5---CERO NO leer"))
if n == 1:
    print(read_h5())
