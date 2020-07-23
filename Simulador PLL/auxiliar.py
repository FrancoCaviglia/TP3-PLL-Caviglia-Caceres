# -*- coding: utf-8 -*-

from numpy import pi, sqrt, sin, cos, convolve, arange, zeros, mod
from numpy.random import random, rand
from scipy import signal
from scipy import fftpack

"""
Created on Thu Jul 16 14:54:36 2020

@author: Franco Caviglia, Joan Joel Cáceres

"""

def rcosfilter(N, alpha, Ts, Fs):
    """
    Generates a raised cosine (RC) filter (FIR) impulse response.
 
    Parameters
    ----------
    N : int
        Length of the filter in samples.
 
    alpha : float
        Roll off factor (Valid values are [0, 1]).
 
    Ts : float
        Symbol period in seconds.
 
    Fs : float
        Sampling Rate in Hz.
 
    Returns
    -------
 
    h_rc : 1-D ndarray (float)
        Impulse response of the raised cosine filter.
 
    time_idx : 1-D ndarray (float)
        Array containing the time indices, in seconds, for the impulse response.
    """
 
    T_delta = 1/float(Fs)
    time_idx = ((arange(N)-N/2))*T_delta
    sample_num = arange(N)
    h_rc = zeros(N, dtype=float)
 
    for x in sample_num:
        t = (x-N/2)*T_delta
        if t == 0.0:
            h_rc[x] = 1.0
        elif alpha != 0 and t == Ts/(2*alpha):
            h_rc[x] = (pi/4)*(sin(pi*t/Ts)/(pi*t/Ts))
        elif alpha != 0 and t == -Ts/(2*alpha):
            h_rc[x] = (pi/4)*(sin(pi*t/Ts)/(pi*t/Ts))
        else:
            h_rc[x] = (sin(pi*t/Ts)/(pi*t/Ts))*(cos(pi*alpha*t/Ts)/(1-(((2*alpha*t)/Ts)*((2*alpha*t)/Ts))))
 
    return time_idx, h_rc

def delta_0(m, t0, N, Ts):

    salida = [ ]

    for t in arange(0,N*Ts,Ts):
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
        salida.append([t, sin(2*pi*f0*t+fase_inicial)])
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

    entrada = []        # Para separar la variable dependiente en los pares (x,y)
    salida  = []        # Para armar la lista con los pares (x,y) filtrados

    for elem in xd:     # Primero construye un array para poder pasarlo al filtro
        entrada.append(elem[1])  

    coeficientes = coef_filtro(tipo, C, R1, R2, Ts)
    
    if zi == []:        # Por si se desea filtrar toda una señal en una unica ejecución.
        zi = entrada[0]*signal.lfilter_zi(coeficientes[0], coeficientes[1])
    else:
        pass

    for i in range(len(xd)):
  
        filtrado, zi = signal.lfilter(coeficientes[0], coeficientes[1], [entrada[i]], zi=zi )
        salida.append([xd[i][0], filtrado[0]]) # Arma la lista con coordenadas (t,V)
        
    return salida, zi

def traductor(tipo, omega, xi):
    
    if tipo == 'rc':
        R = sqrt(2*xi*omega)
    elif tipo == 'lead-lag activo':
        R = sqrt(2*xi/omega)
    else:
        return 0
    return R

def filtro_traducido(xd, estado_inicial, tipo, omega, xi, Ts):

    """ Transforma los parámetros de entrada para el filtro de R1, R2, C en Xi, Omega. """

    R = traductor(tipo, xi, omega)
    return filtro(xd, estado_inicial, tipo, R, R, R, Ts)

def fase(Ts, f, fase_inicial):
    
    fase = fase_inicial + 2*pi*f*Ts  # Calcula la fase según la fórmula (10)
    fase_final = mod(fase, 2*pi)     # Asegura que el valor esté en (0, 2pi)
    
    return fase_final

def vco(v, Ts, K, f0, ph):
    
    if ph == None:
        ph = 2*pi*f0*v[0][0]
    else:
        pass
    
    salida = []
   
    for i in range(len(v)):
        ph = fase(Ts, f0+K*v[i][1], ph)
        salida.append( [ v[i][0]+Ts, sin(ph) ] )
    
    return salida, ph

def PLL(xr, tipo, xi, omega, f0, K, Ts):
    
    # Primero arma la condición inicial
    
    R = traductor(tipo, xi, omega)
    coeficientes = coef_filtro(tipo, R, R, R, Ts)
    
    xd = [[0,0]]
    xc = [[0,0]] # Antes de entrar la señal, los pasos intermedios son cero
    xv = [[0,0]] # Para el detector de fase
    ph = 0       # fase de la salida inicial del VCO, xv

    zi = xd[0][1]*signal.lfilter_zi(coeficientes[0], coeficientes[1])

    for i in range(len(xr)):                              # Itera sobre cada elemento 
        xd.append(detector([xr[i]], [xv[-1]])[-1])        # 1ro. el detector de fase
        xc_, zi = filtro([xd[-1]], zi, tipo, R, R, R, Ts) # 2do. el filtro
        xc.append(xc_[-1])
        xv_, ph = vco([xc[-1]], Ts, K, f0, ph)            # 3ro. el VCO
        xv.append(xv_[-1])
        
    return xr, xd, xc, xv

def fuente_fvar(f_inicial, f_final, Ts, fase_inicial, N):
    
    salida = []
    m = (f_final-f_inicial)/(N-1)                                    # Se puede dividir por tiempo. En ese caso hay que corregir por que se multiplica abajo.

    for i in range(N):
        
        f = f_inicial+m*i
        salida.append([i*Ts,sin(2*pi*f*i*Ts + fase_inicial)])  # Añade un nuevo punto a la lista.

    return salida

def gen_cod(Nd, Ts, Tb):

    salida = []
    step = int(Tb/Ts)
    
    for j in range(0, int(step/2)):
            salida.append([j*Ts, 0])

    for i in range(0, Nd):
        salida.append( [ (i*step+int(step/2))*Ts, round(rand()) ] )        
        
        if i<(Nd-1):
            for j in range(i*step+int(step/2)+1, (i+1)*step+int(step/2)):
                salida.append([j*Ts, 0])
        if i==(Nd-1):
            for j in range(i*step+int(step/2)+1, (i+1)*step):
                salida.append([j*Ts, 0])
                
    return salida

def respuesta_filtro(N, a, Tb, Fs):

    lista = rcosfilter(N, a, Tb, Fs)

    respuesta = []

    for i in range(N):
        respuesta.append([lista[0][i], lista[1][i]])

    return respuesta

def multiplicador(x,y):
    salida = []
    for i in range(len(x)):
        salida.append([x[i][0], x[i][1]*y[i][1]])
    return salida