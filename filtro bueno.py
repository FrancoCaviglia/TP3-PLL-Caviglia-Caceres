# -*- coding: utf-8 -*-

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

entrada = []
tn = []

for t in np.arange(0,50,0.0001):
    tn.append(t)
    entrada.append(np.sin(2*np.pi*0.05*t) + np.sin(2*np.pi*1.0*t)+1 )

def filtro(xd, zi):
    salida = []
    for i in range(len(xd)):
        dato, zi = signal.lfilter(coeficientes[0], coeficientes[1], [xd[i]], zi=zi)
        salida.append(dato[0]) # Arma la lista con coordenadas (t,V)
    return salida, zi

R1 = 1.1
C = 1.1
Ts = 0.0001

coeficientes = signal.bilinear([1], [R1*C, 1], 1/Ts)

zi = entrada[0]*signal.lfilter_zi(coeficientes[0], coeficientes[1])
salida = []
control_0 = []
for i in range(len(entrada)):
    dato, zi = filtro([entrada[i]], zi)
    salida.append(dato[-1])

zi = entrada[0]*signal.lfilter_zi(coeficientes[0], coeficientes[1])
salida_1, zx = filtro(entrada, zi)

plt.figure()

plt.plot(tn, entrada, 'b') # Azul
plt.plot(tn, salida, 'r') # Azul
plt.plot(tn, salida_1, 'k') # Azul

plt.show()