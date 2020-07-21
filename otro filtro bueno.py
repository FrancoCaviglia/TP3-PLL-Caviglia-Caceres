# -*- coding: utf-8 -*-

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

tn = []
xn = []
for i in range(100):
    tn.append(i/100)
    xn.append(np.sin(2*np.pi*0.75*tn[i]*(1-tn[i]) + 2.1) + 0.1*np.sin(2*np.pi*1.25*tn[i] + 1) + 0.18*np.cos(2*np.pi*3.85*tn[i]) + np.random.random()*0.08)
 #   xn.append(np.sin(2*np.pi*0.01*tn[i]) + np.sin(2*np.pi*0.10*tn[i]) )

def filtro(xd, zi):
    salida = []
    for i in range(len(xd)):
        dato, zi = signal.lfilter(coeficientes[0], coeficientes[1], [xd[i]], zi=zi)
        salida.append(dato[0]) # Arma la lista con coordenadas (t,V)
    return salida, zi

coeficientes = signal.bilinear([1], [2, 1], 1/0.001)

zi = xn[0]*signal.lfilter_zi(coeficientes[0], coeficientes[1])

yn = []
for i in range(len(xn)):
    salida, zi = filtro([xn[i]], zi)
    yn.append(salida[-1])

plt.figure()

plt.plot(tn, xn, 'b') # Azul
plt.plot(tn, yn, 'r') # Roja

plt.show()