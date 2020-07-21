# -*- coding: utf-8 -*-

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

tn = []
xn = []

samples = 201
for i in range(samples):
    tn.append(-1+2*i/samples)
for i in range(len(tn)):
    #xn.append(np.sin(2*np.pi*tn[i]) + np.sin(2*np.pi*10*tn[i]) + 3)
    xn.append(np.sin(2*np.pi*0.75*tn[i]*(1-tn[i]) + 2.1) + 0.1*np.sin(2*np.pi*1.25*tn[i] + 1) + 0.18*np.cos(2*np.pi*3.85*tn[i]) + np.random.random()*0.3)

R1 = 4.6
C = 4.6
Ts = 1/samples

coeficientes = signal.bilinear([19], [1, 19], 1/Ts)
print(coeficientes)

def filtro_1(entrada):

    filtrado = signal.lfilter(coeficientes[0], coeficientes[1], entrada)

    return filtrado.tolist()

def filtro_2(entrada):

    zi = signal.lfilter_zi(coeficientes[0], coeficientes[1])    
    
    filtrado = signal.lfilter(coeficientes[0], coeficientes[1], entrada, zi=zi)
    
    return filtrado[0].tolist(), filtrado[1].tolist()
    
def filtro_3(entrada):

    salida = []
    zi = signal.lfilter_zi(coeficientes[0], coeficientes[1])  
    juego = []
    for i in range(len(entrada)):
        juego.append(zi)        
        filtrado, zi = signal.lfilter(coeficientes[0], coeficientes[1], [entrada[i]], zi=zi)
        salida.append(filtrado[-1])

    return salida, juego

def filtro_4(entrada):

    salida = []
    zi = signal.lfiltic(coeficientes[0], coeficientes[1], [0])  

    for i in range(len(entrada)):
        
        filtrado, zi = signal.lfilter(coeficientes[0], coeficientes[1], [entrada[i]], zi=zi)
        salida.append(filtrado[-1])

    return salida

def filtro_5(entrada):

    zi = signal.lfiltic(coeficientes[0], coeficientes[1], [0])  
    filtrado, _ = signal.lfilter(coeficientes[0], coeficientes[1], entrada, zi=zi*entrada[0])

    return filtrado.tolist()

def filtro_5_bis(entrada):

    zi = signal.lfiltic(coeficientes[0], coeficientes[1], [entrada[0]])  
    filtrado, _ = signal.lfilter(coeficientes[0], coeficientes[1], entrada, zi=zi)

    return filtrado.tolist()

def filtro_6(entrada):

    zi = entrada[0]*signal.lfilter_zi(coeficientes[0], coeficientes[1])  
    salida = []
    
    for i in range(len(entrada)):
        filtrado, zi = signal.lfilter(coeficientes[0], coeficientes[1], [entrada[i]], zi=zi)
        salida.append(filtrado.tolist()[-1])
    return salida

def filtro_6_bis(entrada, zi):

    salida = []
    
    for i in range(len(entrada)):
        filtrado, zi = signal.lfilter(coeficientes[0], coeficientes[1], [entrada[i]], zi=zi)
        salida.append(filtrado.tolist()[-1])
    return salida, zi

yn = filtro_1(xn)       # No iteran
zn = filtro_2(xn)[0]      # No iteran
wn = filtro_3(xn)[0]       # Iteran
vn = filtro_4(xn)       # Iteran 
un = filtro_5(xn)       # No iteran
en = filtro_5_bis(xn)   # No iteran
qn = filtro_6(xn)       # No iteran

salida_6 = []
for i in range(len(xn)):
    salida_6.append(filtro_6([xn[i]]))
    #print([xn[i]], filtro_6([xn[i]]))

""" """
zi = xn[0]*signal.lfilter_zi(coeficientes[0], coeficientes[1])  
print(zi) 
salida_6_bis = []
zi_1 = []
for i in range(len(xn)):
    zi_1.append(zi)
    datos, zi = filtro_6_bis([xn[i]], zi)
    salida_6_bis.append(datos[-1])
""" """
zi = signal.lfilter_zi(coeficientes[0], coeficientes[1])  
print(zi) 
salida_6_bis_bis = []
for i in range(len(xn)):
    datos, zi = filtro_6_bis([xn[i]], zi)
    salida_6_bis_bis.append(datos[-1])

zi = signal.lfiltic(coeficientes[0], coeficientes[1], [xn[0]]) 
print(zi)  
salida_6_bis_bis_bis = []
zi_2 = []
for i in range(len(xn)):
    zi_2.append(zi)    
    datos, zi = filtro_6_bis([xn[i]], zi)
    salida_6_bis_bis_bis.append(datos[-1])

zi = signal.lfiltic(coeficientes[0], coeficientes[1], [0])  
print(zi) 
salida_6_bis_bis_bis_bis = []
for i in range(len(xn)):
    datos, zi = filtro_6_bis([xn[i]], zi)
    salida_6_bis_bis_bis_bis.append(datos[-1])

zi = signal.lfiltic(coeficientes[0], coeficientes[1], [0], [xn[0]]) 
print(zi)
salida_6_bis_bis_bis_bis_bis = []
for i in range(len(xn)):
    datos, zi = filtro_6_bis([xn[i]], zi)
    salida_6_bis_bis_bis_bis_bis.append(datos[-1])
    
plt.figure(figsize=(10,5))

plt.plot(tn, xn, 'b') # Inicial
#plt.plot(tn, yn, 'r') # =
plt.plot(tn, zn, 'k') # = =
plt.plot(tn, wn, 'c') # = =
#plt.plot(tn, vn, 'g') # =
#plt.plot(tn, un, 'm') # =
#plt.plot(tn, en, 'g') # = = =
#plt.plot(tn, qn, 'b') # = = = =
#plt.plot(tn, salida_6, 'r')
plt.plot(tn, salida_6_bis, 'g') #-win
plt.plot(tn, salida_6_bis_bis, 'k') # 'c'
plt.plot(tn, salida_6_bis_bis_bis, 'm') #-win lose
plt.plot(tn, salida_6_bis_bis_bis_bis, 'c')
plt.plot(tn, salida_6_bis_bis_bis_bis_bis, 'r')
plt.legend(('original','1','2', '3','4', '5', '5bis', '6', 'salida_6'), loc='best')

plt.show()
"""
for i in range(len(xn)):
    print(zi_1[i], zi_2[i])
for i in range(len(xn)):
    print(filtro_2(xn)[1][i], filtro_3(xn)[1][i])
"""
"""
print(filtro_2(xn)[1])
print('hola')
print(filtro_3(xn)[1])
"""
""" def convers(y_1):
    y_2 = []
    for i in range(len(xn)):
        y_2.append(y_1[i])
    return y_2

yn_2 = convers(yn)
zn_2 = convers(zn)
wn_2 = convers(wn)
vn_2 = convers(vn)
un_2 = convers(un)
en_2 = convers(en)
qn_2 = convers(qn) """