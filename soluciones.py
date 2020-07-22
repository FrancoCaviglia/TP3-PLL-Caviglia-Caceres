# -*- coding: utf-8 -*-

import numpy as np
import random as r
from matplotlib import pyplot as plt
from scipy import signal
from scipy import fftpack
from auxiliar import *

#from nucleo import fuente as fuente

datos_A = [[],[]]
datos_B = [[],[]]
datos_C = [[],[]]
datos_D = [[],[]]

datos = [datos_A, datos_B, datos_C, datos_D]

def delta_0(m, t0, N, Ts):

    salida = [ ]

    for t in np.arange(0,N*Ts,Ts):
        if t == t0:
            salida.append([t,m])
        else:
            salida.append([t,0])
            
    return salida

def unir_lista(v,w):
    
    t = v[-1][0]
    suma = v

    for i in range(len(w)):
        suma.append([t+w[i][0],w[i][1]])

    return suma

def conversor(entrada):
    """ Convierte una señal de la forma [[x,y]] en la forma [[x],[y]] """
    salida = [[],[]]
    for i in range(len(entrada)):
        salida[0].append(entrada[i][0])
        salida[1].append(entrada[i][1])
    return salida
    
def fuente(f0, Ts, fase_inicial, N):
    
    t = 0
    salida = []

    for i in range(N):
        salida.append([t, np.sin(2*np.pi*f0*t+fase_inicial)])
        t+=Ts

    return salida

def detector(xr, xv, K=1): 
    
    producto = []
    
    for i in range(len(xr)):
        producto.append([xr[i][0],K*xr[i][1]*xv[i][1]])
        
    return producto

def coef_filtro(tipo, C, R1, R2, Ts):
    
    if tipo == 'rc':
        return signal.bilinear([1], [R1*C,1], 1/Ts)
    elif tipo == 'lead-lag pasivo':
        return signal.bilinear([1,R2*C], [(R1+R2)*C,1], 1/Ts)
    elif tipo == 'lead-lag activo':
        return signal.bilinear([1,R2*C], [R1*C,1], 1/Ts)
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

def traductor(tipo, xi, omega):
    
    if tipo == 'rc':
        R = np.sqrt(2*xi*omega)
    elif tipo == 'lead-lag activo':
        R = np.sqrt(2*xi/omega)
    else:
        return 0
    return R

def filtro_traducido(xd, estado_inicial, tipo, xi, omega, Ts):

    """ Transforma los parámetros de entrada para el filtro de R1, R2, C en Xi, Omega. """

    R = traductor(tipo, xi, omega)
    return filtro(xd, estado_inicial, tipo, R, R, R, Ts)

def fase(Ts,f,fase_inicial):
    
    fase = fase_inicial + 2*np.pi*f*Ts  # Calcula la fase según la fórmula (10)
    fase_final = np.mod(fase, 2*np.pi)  # Asegura que el valor esté en (0, 2pi)
    
    return fase_final

def vco(v, Ts, K, f0):

    salida = []
    ph = 2*np.pi*f0
   
    for i in range(len(v)):
        ph = fase(Ts, f0+K*v[i][1], ph)
        salida.append( [v[i][0], np.sin(ph)] )
    
    return salida

def PLL(xr, tipo, xi, omega, f0, K, Ts):

    # Primero arma la condición inicial
    
    R = traductor(tipo, xi, omega)
    coeficientes = coef_filtro(tipo, R, R, R, Ts)
    zi = xr[0]*signal.lfilter_zi(coeficientes[0], coeficientes[1])
    
    xd = []
    xc = [[-Ts,0]] # Antes de entrar la señal, los pasos intermedios son cero
    xv = [[-Ts,0]] # Para el detector de fase

    for i in range(len(xr)):                              # Itera sobre cada elemento 
        xd.append(detector([xr[i]], [xv[-1]]))            # 1ro. el detector de fase
        xc_, zi = filtro([xd[-1]], zi, tipo, R, R, R, Ts) # 2do. el filtro
        xc.append(xc_[-1])
        xv.append(vco([xc[-1]], Ts, K, f0)[-1])           # 3ro. el VCO
    
    return xr, xd, xc, xv

def fuente_fvar(f_inicial, f_final, Ts, fase_inicial, N):
    
    salida = []
    m = (f_final-f_inicial)/(N-1)                                    # Se puede dividir por tiempo. En ese caso hay que corregir por que se multiplica abajo.

    for i in range(N):
        
        f = f_inicial+m*i
        salida.append([i*Ts,np.sin(2*np.pi*f*i*Ts + fase_inicial)])  # Añade un nuevo punto a la lista.

    return salida

def gen_cod(Ts, Tb, N):

    salida = []
    step = int(Tb/Ts)

    for i in range(0,N,step):
        valor = np.round(np.random.rand())
        for j in range(i,i+step):  
            salida.append([Ts*j,valor])

    return salida

def respuesta_filtro(N,a,Tb,Fs):

    lista = rcosfilter(N, a, Tb, Fs)

    respuesta = []

    for i in range(N):
        respuesta.append([lista[0][i], lista[1][i]])

    return respuesta

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
def ejercicio_1():
        
    datos[0] = conversor(fuente(10, 0.001, 0, 1000))
    datos[1] = conversor(fuente(10, 0.001, np.pi/2, 1000))
    datos[2] = conversor(fuente(5, 0.001, 0, 1000))
    datos[3] = conversor(fuente(5, 0.001, np.pi/2, 1000))
    
    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_2():

    datos[0] = conversor(fuente(1000, 0.00001, np.pi/2, 1000))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_3():
    
    datos[0] = conversor(unir_lista(fuente(1000, 0.00001, np.pi/2, 500), fuente(1000, 0.00001, 3*np.pi/2, 500)))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
   
    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_4():

    datos[0] = conversor(fuente(2000, 0.00001, np.pi/2, 1000))
    datos[1] = conversor(fuente(1000, 0.00001, 0, 1000))
    datos[2] = conversor(detector(fuente(1000, 0.00001, 0, 1000), fuente(3000, 0.00001, np.pi/2, 1000)))
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_5():

    datos[0] = conversor(fuente(1000, 0.00001, 0, 1000))
    datos[1] = conversor(fuente(1000, 0.00001, np.pi/4, 1000))
    datos[2] = conversor(detector(fuente(1000, 0.00001, 0, 1000), fuente(1000, 0.00001, np.pi/4, 1000)))
    datos[3] = [[],[]]
      
    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_6():

    datos[0] = conversor(fuente(1000, 0.00001, 0, 1000))
    datos[1] = conversor(fuente(1000, 0.00001, np.pi/2, 1000))
    datos[2] = conversor(detector(fuente(1000, 0.00001, 0, 1000), fuente(1000, 0.00001, np.pi/2, 1000)))
    datos[3] = [[],[]]
      
    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_7():
    
    entrada_1 = []
    entrada_2 = []
    
    for t in np.arange(-1,1,0.001):
        entrada_1.append([t, np.sin(2*np.pi*0.75*t*(1-t) + 2.1) + 0.1*np.sin(2*np.pi*1.25*t + 1) + 0.18*np.cos(2*np.pi*3.85*t) + np.random.random()*0.3])
        entrada_2.append([t, np.sin(2*np.pi*t) + 0.5*np.sin(2*np.pi*12*t)])
    
    salida_1 = filtro(entrada_1, None, 'rc', 0.25, 0.25, 0, 0.001)[0]
    salida_2 = filtro(entrada_2, None, 'rc', 0.25, 0.25, 0, 0.001)[0]

    datos[0] = conversor(entrada_1)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(entrada_2)
    datos[3] = conversor(salida_2)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_8():
    
    entrada = delta_0(1, 0.0001, 1000000, 0.0001)

    datos[0] = conversor(entrada)
    datos[1] = conversor(filtro_traducido(entrada, None, 'rc',   2, np.sqrt(2)/2, 0.0001)[0])
    datos[2] = conversor(filtro_traducido(entrada, None, 'rc', 100, np.sqrt(2)/2, 0.0001)[0])
    datos[3] = conversor(filtro_traducido(entrada, None, 'rc',    2,           5, 0.0001)[0])
    
    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_9():
    
    N = 2000
    f = 1000
    
    entrada = detector(fuente(f, 0.00001, 0, N), fuente(f, 0.00001, np.pi/4, N))
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(filtro_traducido(entrada, None, 'rc',   2, np.sqrt(2)/2, 0.000001)[0])
    datos[2] = conversor(filtro_traducido(entrada, None, 'rc', 100, np.sqrt(2)/2, 0.000001)[0])
    datos[3] = conversor(filtro_traducido(entrada, None, 'rc',    2,           5, 0.000001)[0])
        
    return 0    

def ejercicio_10():

    N = 2000
    f = 1000
    
    entrada = detector(fuente(f, 0.00001, 0, N), fuente(f, 0.00001, np.pi/4, N))
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(filtro_traducido(entrada, None, 'lead-lag activo',   2, np.sqrt(2)/2, 0.000001)[0])
    datos[2] = conversor(filtro_traducido(entrada, None, 'lead-lag activo', 100, np.sqrt(2)/2, 0.000001)[0])
    datos[3] = conversor(filtro_traducido(entrada, None, 'lead-lag activo',    2,           5, 0.000001)[0])

    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_11():

    Ts = 0.001
    N  = 1000
    f0 = 5
    K  = 1
    
    entrada_1 = fuente(10, Ts, 0, N)
    salida_1 = []
    fase_ahora = 0
    
    for i in range(1,len(entrada_1),1):
        fase_ahora = fase(Ts,f0+K*entrada_1[i-1][1], fase_ahora)
        salida_1.append([entrada_1[i][0], fase_ahora])

    entrada_2 = fuente(5, Ts, 0, N)
    salida_2 = []
    fase_ahora = 0
    
    for i in range(1,len(entrada_2),1):
        fase_ahora = fase(Ts,f0+K*entrada_2[i-1][1], fase_ahora)
        salida_2.append([entrada_2[i][0], fase_ahora])
      
    datos[0] = conversor(entrada_1)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(entrada_2)
    datos[3] = conversor(salida_2)
    
    return datos, ['Tiempo (s)', 'Fase VCO']

def ejercicio_12():

    N = 1000                    # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fmod = 40                   # Frecuencia de la señal moduladora (o de control)
    fs = 10*f0                  # Frecuencia de muestro
    fase_inicial = 0
    Ts = 1/fs                   # Período de muestreo
    
    onda_mod = fuente(fmod, Ts, fase_inicial, N) # Fabrica la onda moduladora              
    
    datos[0] = conversor(onda_mod)
    datos[1] = [[],[]] #conversor(fourier(onda_mod, Ts))
    datos[2] = [[],[]]
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_13():

    N = 1000                    # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fmod = 40                   # Frecuencia de la señal moduladora (o de control)
    fs = 10*f0                  # Frecuencia de muestro
    fase_inicial = 0
    Ts = 1/fs                   # Período de muestreo
    K = 0
    
    onda_mod = fuente(fmod, Ts, fase_inicial, N) # Fabrica la onda moduladora              

    salida_mod = vco(onda_mod, Ts, K, f0)        # Pasa la onda moduladora por un VCO con K=0

    datos[0] = conversor(onda_mod)
    datos[1] = conversor(salida_mod)             #conversor(fourier(onda_mod, Ts))
    datos[2] = [[],[]]
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_14():

    N = 1000                    # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fmod = 40                   # Frecuencia de la señal moduladora (o de control)
    fs = 10*f0                  # Frecuencia de muestro
    fase_inicial = 0
    Ts = 1/fs                   # Período de muestreo
    K = 100
    
    onda_mod = fuente(fmod, Ts, fase_inicial, N) # Fabrica la onda moduladora              

    salida_mod = vco(onda_mod, Ts, K, f0)        # Pasa la onda moduladora por un VCO con K=0

    datos[0] = conversor(onda_mod)
    datos[1] = conversor(salida_mod)             #conversor(fourier(onda_mod, Ts))
    datos[2] = [[],[]]
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_15():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, np.pi/2, N//2))
    salida_1 = PLL(entrada, 'rc', np.sqrt(2)/2, wn, f0, K, Ts)[1]
    salida_2 = PLL(entrada, 'rc', np.sqrt(2)/2, wn, f0, K, Ts)[1]
    salida_3 = PLL(entrada, 'rc', np.sqrt(2)/2, wn, f0, K, Ts)[1]

    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(salida_2)
    datos[3] = conversor(salida_3)

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_16():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, np.pi/2, N//2))
    salida_1 = PLL(entrada, 'rc', np.sqrt(2)/2, wn, f0, K, Ts)[3]
    salida_2 = PLL(entrada, 'rc', np.sqrt(2)/2, wn, f0, K, Ts)[3]
    salida_3 = PLL(entrada, 'rc', np.sqrt(2)/2, wn, f0, K, Ts)[3]
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(salida_2)
    datos[3] = conversor(salida_3)

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_17():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 120
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, np.pi/2, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, 'rc', np.sqrt(2)/2, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_18():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 40
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, np.pi/2, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, 'lead-lag activo', np.sqrt(2)/2, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_19():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 120
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, np.pi/2, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, 'lead-lag activo', np.sqrt(2)/2, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_20():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 220
    xi = 2
    K  = 1
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, np.pi/4, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_21():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 220
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, np.pi/4, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_22():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 80
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, np.pi/4, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_23():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, np.pi/4, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_24():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    error_fase = np.pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 220                    # Parámetros de los filtros
    xi = 2
    K  = 1
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_25():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    error_fase = np.pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_26():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = np.pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_27():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = np.pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 450                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_28():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = np.pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 450                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_29():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = np.pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_30():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = np.pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 120                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_31():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = np.pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 80                     # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_32():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.03*f0                 # Frecuencia de entrada
    error_fase = np.pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 80                     # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_33():
  
    f0 = 1000
    Ts = 1/(100*f0)
    N  = 1000
    fase_inicial = np.pi/2
    
    salida = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)    #falta valores de N y Ts para que se ejecute.
    
    datos[0] = conversor(salida)
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_34():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fase_inicial = np.pi/2
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 450                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'rc'
    
    entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_35():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fase_inicial = np.pi/2
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_36():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fase_inicial = np.pi/2
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 280                    # Parámetros de los filtros
    xi = np.sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_37():

    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras

    datos[0] = conversor(gen_cod(Ts, Tb, N))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_38():

    Fs = 1
    a = 0.5
    N = 100
    Tb = 20

    datos[0] = conversor(respuesta_filtro(N, a, Tb, Fs))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_39():

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_40():

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_41():

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_42():

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_43():

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_44():

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

def ejercicio_45():    

    return datos, ['Tiempo (s)', 'Amplitud (V)'] 

"""
"Generar ahora una señal de entrada al PLL con el error de fase inicial de π/2, y un error de frecuencia del 10 %. Representar en cada caso la señal de error y el diagrama de Lissajous."
"""