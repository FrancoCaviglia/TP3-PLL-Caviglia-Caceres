# -*- coding: utf-8 -*-

"""

Revisado por última vez el Jueves 23 de Julio a las 18:00 2020.
@author: Franco Caviglia, Joan Joel Cáceres

"""

from numpy import pi, sqrt, sin, cos, convolve, arange, zeros, mod, array
from numpy.random import random, rand
from scipy import signal
from scipy import fftpack

""" En este archivo se encuentran las funciones que hacen al funcionamiento del PLL. Las mismas son utilizadas
    por soluciones.py para armar las respuestas a cada ejercicio. """

def rcosfilter(N, alpha, Ts, Fs):
    """
    Función del paquete commpy. Extraída de 
    commpy.readthedocs.io/en/latest/generated/commpy.filters.rcosfilter.html 
    
    ###########################################################################
    
    Genera la respuesta al impulso de un filtro de coseno alzado (RC, FIR).
 
    Parámetros
    ----------
    N : int
        Longitud del filtro en muestras.
 
    alpha : float
        Roll off factor (Valid values are [0, 1]).
 
    Ts : float
        Symbol period in seconds.
 
    Fs : float
        Sampling Rate in Hz.
 
    Retorna
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

    """ Devuelve un impulso en la posición
    
    Parámetros
    ----------
    m : int
        Altura del pulso.
        
    N : int
        Longitud del impulso en muestras.
 
    t0 : float
        Posición del pico.
 
    Ts : float
        Período de muestreo.
 
    Retorna
    -------   
    salida : list
        Lista de pares (t,x) con el impulso.
    
    """
    salida = [ ]

    for t in arange(0, N*Ts, Ts):
        if t == t0:
            salida.append([t,m])
        else:
            salida.append([t,0])
            
    return salida

def lissajous(v,w):
    """ Devuelve una lista de la forma [[y1], [y2]] necesaria para armar la 
        gráfica de lissajous.
    
    Parámetros
    ----------
    v : list
        Primera lista con pares de la forma [x,y].
        
    w : list
        Segunda lista con pares de la forma [x,y].
        
    Retorna
    -------   
    salida : list
        Lista de la forma [[x],[y]].
    
    """
    salida = [[],[]]
    for i in range(len(v)):
        salida[0].append(v[i][1])
        salida[1].append(w[i][1])    
    return salida

def error(v,w):
    """ Devuelve la diferencia entre dos listas.
    
    Parámetros
    ----------
    v : list
        Primera lista con pares de la forma [x,y].
        
    w : list
        Segunda lista con pares de la forma [x,y].
        
    Retorna
    -------   
    salida : list
        Lista de la forma [[x],[y]].
    
    """    
    salida = [[],[]]
    for i in range(len(v)):
        salida[0].append(v[i][0])
        salida[1].append(v[i][1]-w[i][1])    
    return salida

def unir_lista(v,w):
    """ Devuelve un impulso en la posición
    
    Parámetros
    ----------
    v : list
        Primera lista.
        
    w : list
        Segunda lista.
        
    Retorna
    -------   
    suma : list
        Lista de pares (t,x) con la suma de ambas listas.
    
    """    
    t = v[-1][0]
    suma = v

    for i in range(len(w)):
        suma.append([t+w[i][0],w[i][1]])
    return suma

def conversor(entrada):
    """ Convierte una señal de la forma [[x,y]] en la forma [[x],[y]].
    
    Parámetros
    ----------
    entrada : list
              Lista con pares de la forma (x,y)
              
    Retorna
    -------   
    salida : list
            Lista con dos elementos [x], [y] con cada valor x[i], y[i].
    
    """
    salida = [[],[]]
    for i in range(len(entrada)):
        salida[0].append(entrada[i][0])
        salida[1].append(entrada[i][1])
    return salida
    
def fuente(f0, Ts, fase_inicial, N):

    """ Retorna una lista con pares de valores [ x, sen(f0 x + fase_inicial) ].
    
    Parámetros
    ----------
    f0 : float
        Frecuencia en Hz.
    Ts : float
        Período de muestreo en segundos.
    fase_inicial : float
        Fase inicial.
    N : int
        Cantidad de muestras.
              
    Retorna
    -------   
    salida : list
        Lista con N elementos de la forma de los pares ordenados [x, y].
    
    """    
    t = 0
    salida = []

    for i in range(N):
        salida.append([t, sin(2*pi*f0*t+fase_inicial)])
        t+=Ts

    return salida

def detector(xr, xv, K=1): 
    """ Retorna una lista con pares de valores dados por el producto de ambas señales..
    
    Parámetros
    ----------
    xr : list
        Señal de entrada de la forma [[x,y]] con N elementos.
    xv : list
        Señal de entrada de la forma [[x,y]] con N elementos.
    K  : float
        Opcional. Ganancia. 
              
    Retorna
    -------   
    producto : list
        Lista con N elementos de la forma de los pares ordenados [x, y].
    
    """
    producto = []
    
    for i in range(len(xr)):
        producto.append([xr[i][0],K*xr[i][1]*xv[i][1]])
        
    return producto

def coef_filtro(tipo, C, R1, R2, Ts):
    """ Retorna una lista con los coeficientes del filtro según sus parámetros.
    
    Parámetros
    ----------
    tipo : str
        Tipo de filtro que cuyos parámetros se desean obtener.
    C : float
        Valor del capacitor en el filtro.
    R1 : float
        Valor de la resistencia del filtro.
    R2 : float
        Valor de la resistencia del filtro.
    Ts : float
        Período de muestreo de la señal a filtrar en segundos.
    
    Retorna
    -------   
    signal.bilinear() : list de narray.
        Lista con los coeficientes del numerador y denominador.
    
    """    
    if tipo == 'rc':
        return signal.bilinear([1], [R1*C,1], 1/Ts)
    elif tipo == 'lead-lag pasivo':
        return signal.bilinear([R2*C,1], [(R1+R2)*C,1], 1/Ts)
    elif tipo == 'lead-lag activo':
        return signal.bilinear([R2*C,1], [R1*C,0], 1/Ts)
    else:
        return 0

def filtro(xd, zi, tipo, C, R1, R2, Ts):
    """ Retorna una lista con los coeficientes del filtro según sus parámetros.
    
    Parámetros
    ----------
    xd : list
        Lista con pares de la forma [[x,y]] que representa la señal a filtrar.
    zi : array
        Condición inicial para el filtro. Si ninguna es dada, entonces la cálcula.
    tipo : str
        Tipo de filtro que se desea utilizar.
    C : float
        Valor del capacitor en el filtro.
    R1 : float
        Valor de la resistencia del filtro.
    R2 : float
        Valor de la resistencia del filtro.
    Ts : float
        Período de muestreo de la señal a filtrar en segundos.
    
    Retorna
    -------   
    salida : list
        Lista con la señal filtrada de la forma [[x,y]]
    zi : array
        Último parámetro inicial devuelto por signal.lfilter().
    
    """
    entrada = []        # Para separar la variable dependiente en los pares (x,y)
    salida  = []        # Para armar la lista con los pares (x,y) filtrados
    
    for elem in xd:     # Primero construye un array para poder pasarlo al filtro
        entrada.append(elem[1])
    
    coeficientes = coef_filtro(tipo, C, R1, R2, Ts)

    if zi == []:        # Por si se desea filtrar toda una señal en una única ejecución.
        zi = entrada[0]*signal.lfiltic(coeficientes[0], coeficientes[1],[0])
    else:
        pass
    
    for i in range(len(xd)):
        
        filtrado, zi = signal.lfilter(coeficientes[0], coeficientes[1], [entrada[i]], zi=zi )
        salida.append([xd[i][0], filtrado[0]]) # Arma la lista con coordenadas (t,V)
        
    return salida, zi

def traductor(tipo, omega, xi):
    """ Retorna una lista con los parámetros C, R1, R2 de un filtro tipo según el 
        factor de amortiguamiento xi, y la pulsación propia omega. Se asume C = R1 = R2.
    
    Parámetros
    ----------
    tipo : str
        Tipo de filtro cuyos parámetros se desea calcular.
    omega : float
        Pulsación propia del filtro.
    xi : str
        Factor de amortiguamiento.
        
    Retorna
    -------   
    R : float
        Resistencia del filtro. R = C = R1 = R2.

    """    
    if tipo == 'rc':
        R = 1/sqrt(2*xi*omega)
    elif tipo == 'lead-lag activo':
        R = sqrt(2*xi*omega)
    else:
        return 0
    return R

def filtro_traducido(xd, estado_inicial, tipo, omega, xi, Ts):

    """ Transforma los parámetros de entrada para el filtro de R1, R2, C en xi, omega.
    
    Parámetros
    ----------
    xd : list
        Lista con pares de la forma [[x,y]] que representa la señal a filtrar.
    zi : array
        Condición inicial para el filtro. Si ninguna es dada, entonces la cálcula.
    tipo : str
        Tipo de filtro que se desea utilizar.
    omega : float
        Pulsación propia.
    xi : float
        Factor de amortiguamiento.
    Ts : float
        Período de muestreo de la señal a filtrar en segundos.
        
    Retorna
    -------   
    filtro() : list
        Ver retorno de la función filtro().

    """    
    
    R = traductor(tipo, omega, xi)
    return filtro(xd, estado_inicial, tipo, R, R, R, Ts)

def fase(Ts, f, fase_inicial):
    
    """ Retorna la fase en el instante siguiente dada la fase inicial en el VCO. 
    
    Parámetros
    ----------
    Ts : float
        Período de muestreo del sistema.
    f : float
        Frecuencia de oscilación natural de VCO.
    fase_inicial : float
        Fase inicial de la salida del VCO.

    Retorna
    -------   
    fase_inicial : float
        Fase de la salida del VCO en la muestra siguiente.

    """ 
    fase = fase_inicial + 2*pi*f*Ts  # Calcula la fase según la fórmula (10)
    fase_final = mod(fase, 2*pi)     # Asegura que el valor esté en (0, 2pi)
    
    return fase_final

def vco(xc, Ts, K, f0, ph):
    
    """ Retorna la salida del VCO dada la señal de entrada v sus parámetros.. 
    
    Parámetros
    ----------
    xc : list
        Señal de entrada representada con una lista con N elementos de la forma [x,y].
    Ts : float
        Período de muestreo de la señal de entrada.
    K : float
        Ganancia de lazo del VCO.
    f0 : float
        Frecuencia de oscilación natural del VCO.
    ph : float
        Fase inicial de la salida del VCO.
        
    Retorna
    -------   
    V_vco : lista
        Señal de salida representada con una lista con N elementos de la forma [x,y].
    ph : fase del último elemento de V_vco. Sirve si se quiere iterar fuera de la función.
    
    """     
    if ph == None:
        ph = 2*pi*f0*xc[0][0]
    else:
        pass
    
    V_vco = []
   
    for i in range(len(xc)):
        ph = fase(Ts, f0+K*xc[i][1], ph)
        V_vco.append( [ xc[i][0]+Ts, sin(ph) ] )
    
    return V_vco, ph

def PLL(xr, tipo, xi, omega, f0, Ts):
    
    """ Retorna las salidas del PLL dada la condición inicial y sus parámetros. 
    
    Parámetros
    ----------
    xr : list
        Señal de entrada representada con una lista con N elementos de la forma [x,y].
    Tipo : str
        Filtro que se utiliza dentro del PLL.
    xi : float
        Coeficiente de amortiguamiento del filtro.
    omega : float
        Pulsación propia del filtro.
    f0 : float
        Frecuencia de oscilación natural del VCO.
    Ts : float
        Período de muestreo de la señal de entrada.

    Retorna
    -------   
    xr : list
        Señal de entrada representada con una lista con N elementos de la forma [x,y].
    xd : list
        Señal de salida del detector de fase.
    xc : list
        Señal de salida del filtro.
    xv : list
        Señal de salida del VCO.
    """    
    
    R = traductor(tipo, omega, xi)                      # Primero arma la condición inicial
    coeficientes = coef_filtro(tipo, R, R, R, Ts)
    
    if tipo == 'rc':                # Calcula la ganancia de lazo del VCO
        K = omega/(2*xi)
    elif tipo == 'lead-lag activo':
        K = 2*xi*omega
        
    xd = [[0,0]]
    xc = [[0,0]] # Antes de entrar la señal, los pasos intermedios son cero
    xv = [[0,0]] # Para el detector de fase
    ph = 0       # fase de la salida inicial del VCO, xv

    zi = xd[0][1]*signal.lfiltic(coeficientes[0], coeficientes[1],[0])

    for i in range(len(xr)):                              # Itera sobre cada elemento 
        xd.append(detector([xr[i]], [xv[-1]])[-1])        # 1ro. el detector de fase
        xc_, zi = filtro([xd[-1]], zi, tipo, R, R, R, Ts) # 2do. el filtro
        xc.append(xc_[-1])
        xv_, ph = vco([xc[-1]], Ts, K, f0, ph)            # 3ro. el VCO
        xv.append(xv_[-1])
        
    return xr, xd, xc, xv, K

def fuente_fvar(f_inicial, f_final, Ts, fase_inicial, N):
    """ Retorna una señal de la forma [[x,y]] con un seno con una rampa de frecuencia. 
    
    Parámetros
    ----------
    f_inicial : float
        Frecuencia inicial para la rampa de frecuencia.
    f_final : float
        Frecuencia final para la rampa de frecuencia.
    Ts : float
        Período de muestreo de la señal de salida.
    fase_inicial : float
        Fase inicial del seno dentro del cual se usará la rampa de frecuencia.
    N : int
        Cantidad de muestras de la salida.
        
    Retorna
    -------   
    salida : list
        Señal de salida representada con una lista con N elementos de la forma [x,y].

    """       
    salida = []
    m = (f_final-f_inicial)/(N-1)                                    # Se puede dividir por tiempo. En ese caso hay que corregir por que se multiplica abajo.

    for i in range(N):
        
        f = f_inicial+m*i
        salida.append([i*Ts,sin(2*pi*f*i*Ts + fase_inicial)])  # Añade un nuevo punto a la lista.

    return salida

def gen_cod(Nd, Ts, Tb):
    """ Retorna una señal de la forma [[x,y]] con una serie de impulsos. 
    
    Parámetros
    ----------
    Nd : int
        Cantidad de símbolos.
    Ts : float
        Período de muestreo de la señal de salida en segundos.
    Tb : float
        Período entre símbolos de la señal de salida en segundos.
        
    Retorna
    -------   
    salida : list
        Señal de salida representada con una lista con N = Nd*Tb/Ts elementos de la forma [x,y].

    """     
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
    """ Retorna una señal de la forma [[x,y]] con una serie de impulsos. 
    
    Parámetros
    ----------
    N : int
        Longitud de la respuesta en cantidad de muestras.
    a : float
        Parámetro del filtro de coseno alzado (factor del roll-off). Comprendido entre 0 y 1.
    Tb : float
        Período entre símbolos de la señal de salida en segundos.
    Fs : float
        Frecuencia de muestreo del filtro.
                
    Retorna
    -------   
    respuesta : list
        Señal de salida representada con una lista con N elementos de la forma [x,y].

    """    
    lista = rcosfilter(N, a, Tb, Fs)

    respuesta = []

    for i in range(N):
        respuesta.append([lista[0][i], lista[1][i]])

    return respuesta