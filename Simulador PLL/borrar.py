# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

def conversor(entrada):
    """ Convierte una señal de la forma [[x,y]] en la forma [[x],[y]] """
    salida = [[],[]]
    for i in range(len(entrada)):
        salida[0].append(entrada[i][0])
        salida[1].append(entrada[i][1])
    return salida

def coef_filtro(tipo, C, R1, R2, Ts):
    
    if tipo == 'rc':
        return signal.bilinear([1], [R1*C, 1], 1/Ts)
    elif tipo == 'lead-lag pasivo':
        return signal.bilinear([1,R2*C], [1,(R1+R2)*C], 1/Ts)
    elif tipo == 'lead-lag activo':
        return signal.bilinear([1,R2*C], [0,R1*C], 1/Ts)
    else:
        return 0

def filtro(xd, zi, tipo, C, R1, R2, Ts):

    entrada = []          # Para separar la variable dependiente en los pares (x,y)
    salida = []           # Para armar la lista con los pares (x,y) filtrados

    for elem in xd:       # Primero construye un array para poder pasarlo al filtro
        entrada.append(elem[1])  

    coeficientes = coef_filtro(tipo, C, R1, R2, Ts)
    
    if zi == None:        # Por si se desea filtrar toda una señal en una unica ejecución.
        zi = entrada[0]*signal.lfilter_zi(coeficientes[0], coeficientes[1])
    else:
        pass

    for i in range(len(xd)):
  
        filtrado, zi = signal.lfilter(coeficientes[0], coeficientes[1], [entrada[i]], zi=zi )
        salida.append([xd[i][0], filtrado[0]]) # Arma la lista con coordenadas (t,V)
        
    return salida, zi

entrada_1 = []
entrada_2 = []
entrada_3 = []
   
for t in np.arange(-1,1,0.001):
    entrada_1.append([t, np.sin(2*np.pi*0.75*t*(1-t) + 2.1) + 0.1*np.sin(2*np.pi*1.25*t + 1) + 0.18*np.cos(2*np.pi*3.85*t) + np.random.random()*0.2])
    entrada_2.append([t, np.sin(2*np.pi*t) + 0.5*np.sin(2*np.pi*12*t)])
    entrada_3.append([t, np.sin(16*t)])
    
salida_1 = filtro(entrada_1, None, 'rc', 0.25, 0.25, 0, 0.001)[0]
salida_2 = filtro(entrada_2, None, 'rc', 0.25, 0.25, 0, 0.001)[0]
salida_3 = filtro(entrada_3, None, 'rc', 0.25, 0.25, 0, 0.001)[0]
convertido_entrada_1 = conversor(entrada_1)
convertido_salida_1  = conversor(salida_1)
convertido_entrada_2 = conversor(entrada_2)
convertido_salida_2  = conversor(salida_2)
convertido_entrada_3 = conversor(entrada_3)
convertido_salida_3  = conversor(salida_3)
"""
frq = [0.00001,0.0001,0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000]
w, h = signal.freqs(coef_filtro('rc', 0.1, 0.1, 0,0.001)[0], coef_filtro('rc',0.1,0.1,0,0.001)[1], frq)
print(h[8])
plt.plot(w/(2*np.pi), 20 * np.log10(abs(h)), 'b')
plt.xscale('log')
"""
plt.figure()
plt.plot(convertido_entrada_1[0], convertido_entrada_1[1], 'b')
plt.plot(convertido_salida_1[0], convertido_salida_1[1], 'r')
plt.show()

plt.figure()
plt.plot(convertido_entrada_2[0], convertido_entrada_2[1], 'b')
plt.plot(convertido_salida_2[0], convertido_salida_2[1], 'r')
plt.show()

plt.figure()
plt.plot(convertido_entrada_3[0], convertido_entrada_3[1], 'b')
plt.plot(convertido_salida_3[0], convertido_salida_3[1], 'r')
    
plt.show()