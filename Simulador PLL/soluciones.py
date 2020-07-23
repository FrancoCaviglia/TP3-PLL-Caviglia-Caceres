# -*- coding: utf-8 -*-

from auxiliar import *

datos = [ [[],[]], [[],[]], [[],[]], [[],[]]]
param = [1000, 1000000, 1000, 0, sqrt(2)/2, 0.3, 2, 1, 1000, 'rc']

def ejercicio_1():
        
    datos[0] = conversor(fuente(10, 0.001, 0, 1000))
    datos[1] = conversor(fuente(10, 0.001, pi/2, 1000))
    datos[2] = conversor(fuente(5, 0.001, 0, 1000))
    datos[3] = conversor(fuente(5, 0.001, pi/2, 1000))
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_2():
    
    N  = 1000
    f0 = 1000
    fs = 100*f0
    Ts = 1/fs
    
    datos[0] = conversor(fuente(f0, Ts, pi/2, N))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_3():
    
    N  = 1000
    f0 = 1000
    fs = 100*f0
    Ts = 1/fs
    fase_inicial = pi/2
    
    datos[0] = conversor(unir_lista(fuente(f0, Ts, fase_inicial, N//2), fuente(f0, Ts, fase_inicial + pi, N//2)))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
   
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_4():

    entrada_1 = fuente(200, 0.00001, pi/2, 1000)
    entrada_2 = fuente(100, 0.00001, 0, 1000)
    
    datos[0] = conversor(entrada_1)
    datos[1] = conversor(entrada_2)
    datos[2] = conversor(detector(entrada_1, entrada_2))
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_5():

    N  = 1000
    f0 = 1000
    Ts = 1/(100*f0)
    fase_1 = 0
    fase_2 = pi/4
    
    entrada_1 = fuente(f0, Ts, fase_1, N)
    entrada_2 = fuente(f0, Ts, fase_2, N)
    
    datos[0] = conversor(entrada_1)
    datos[1] = conversor(entrada_2)
    datos[2] = conversor(detector(entrada_1, entrada_2))
    datos[3] = [[],[]]
      
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_6():

    N  = 1000
    f0 = 1000
    Ts = 1/(100*f0)
    fase_1 = 0
    fase_2 = pi/2
    
    entrada_1 = fuente(f0, Ts, fase_1, N)
    entrada_2 = fuente(f0, Ts, fase_2, N)
    
    datos[0] = conversor(entrada_1)
    datos[1] = conversor(entrada_2)
    datos[2] = conversor(detector(entrada_1, entrada_2))
    datos[3] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_7():
    
    entrada_1 = []
    entrada_2 = []
    
    for t in arange(-1,1,0.001):
        entrada_1.append([t, sin(2*pi*0.75*t*(1-t) + 2.1) + 0.1*sin(2*pi*1.25*t + 1) + 0.18*cos(2*pi*3.85*t) + random()*0.3])
        entrada_2.append([t, sin(2*pi*t) + 0.5*sin(2*pi*12*t)])
    
    salida_1 = filtro(entrada_1, None, 'rc', 0.25, 0.25, 0, 0.001)[0]
    salida_2 = filtro(entrada_2, None, 'rc', 0.25, 0.25, 0, 0.001)[0]

    datos[0] = conversor(entrada_1)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(entrada_2)
    datos[3] = conversor(salida_2)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_8():
    
    entrada = delta_0(1, 0.0001, 1000000, 0.0001)

    datos[0] = conversor(entrada)
    datos[1] = conversor(filtro_traducido(entrada, None, 'rc',   2, sqrt(2)/2, 0.0001)[0])
    datos[2] = conversor(filtro_traducido(entrada, None, 'rc', 100, sqrt(2)/2, 0.0001)[0])
    datos[3] = conversor(filtro_traducido(entrada, None, 'rc',    2,           5, 0.0001)[0])
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_9():
    
    N = 2000
    f = 1000
    
    entrada = detector(fuente(f, 0.00001, 0, N), fuente(f, 0.00001, pi/4, N))
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(filtro_traducido(entrada, None, 'rc',   2, sqrt(2)/2, 0.000001)[0])
    datos[2] = conversor(filtro_traducido(entrada, None, 'rc', 100, sqrt(2)/2, 0.000001)[0])
    datos[3] = conversor(filtro_traducido(entrada, None, 'rc',    2,           5, 0.000001)[0])
        
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param  

def ejercicio_10():

    N = 2000
    f = 1000
    
    entrada = detector(fuente(f, 0.00001, 0, N), fuente(f, 0.00001, pi/4, N))
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(filtro_traducido(entrada, None, 'lead-lag activo',   2, sqrt(2)/2, 0.000001)[0])
    datos[2] = conversor(filtro_traducido(entrada, None, 'lead-lag activo', 100, sqrt(2)/2, 0.000001)[0])
    datos[3] = conversor(filtro_traducido(entrada, None, 'lead-lag activo',    2,           5, 0.000001)[0])

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

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

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

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

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

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

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_15():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    salida_1 = PLL(entrada, 'rc', sqrt(2)/2, wn, f0, K, Ts)[1]
    salida_2 = PLL(entrada, 'rc', sqrt(2)/2, wn, f0, K, Ts)[1]
    salida_3 = PLL(entrada, 'rc', sqrt(2)/2, wn, f0, K, Ts)[1]

    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(salida_2)
    datos[3] = conversor(salida_3)

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_16():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    salida_1 = PLL(entrada, 'rc', sqrt(2)/2, wn, f0, K, Ts)[3]
    salida_2 = PLL(entrada, 'rc', sqrt(2)/2, wn, f0, K, Ts)[3]
    salida_3 = PLL(entrada, 'rc', sqrt(2)/2, wn, f0, K, Ts)[3]
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(salida_2)
    datos[3] = conversor(salida_3)

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_17():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 120
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, 'rc', sqrt(2)/2, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_18():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 40
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, 'lead-lag activo', sqrt(2)/2, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_19():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 120
    K  = 1
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, 'lead-lag activo', sqrt(2)/2, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

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
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/4, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_21():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 220
    xi = sqrt(2)/2
    K  = 1
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/4, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_22():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 80
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/4, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_23():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/4, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_24():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    error_fase = pi
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

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_25():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]

    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_26():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_27():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 450                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_28():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 450                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_29():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_30():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 120                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_31():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 80                     # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_32():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.03*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 80                     # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_33():
  
    f0 = 1000
    Ts = 1/(100*f0)
    N  = 1000
    fase_inicial = pi/2
    
    salida = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)    #falta valores de N y Ts para que se ejecute.
    
    datos[0] = conversor(salida)
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_34():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fase_inicial = pi/2
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 450                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'rc'
    
    entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_35():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fase_inicial = pi/2
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_36():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fase_inicial = pi/2
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 280                    # Parámetros de los filtros
    xi = sqrt(2)/2
    K  = 1
    tipo = 'lead-lag activo'
    
    entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)
    _, _, salida_filtro, salida_vco = PLL(entrada, tipo, xi, wn, f0, K, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
 
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param

def ejercicio_37():

    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras

    datos[0] = conversor(gen_cod(Nd, Ts, Tb))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_38():

    Fs = 1
    a = 0.5
    N = 100
    Tb = 2

    datos[0] = conversor(respuesta_filtro(N, a, Tb, Fs))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_39():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5
    
    datos[0] = conversor(convolve(gen_cod(Nd, Ts, Tb), respuesta_filtro(N, a, Tb, Fs), 'same'))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_40():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 1          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5
    
    datos[0] = conversor(convolve(gen_cod(Nd, Ts, Tb), respuesta_filtro(N, a, Tb, Fs), 'same'))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_41():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5
    f0 = 1000
    
    entrada    = gen_cod(Nd, Ts, Tb)
    filtrado   = convolve(entrada, respuesta_filtro(N, a, Tb, Fs), 'same')
    moduladora = fuente(f0,Ts,0,N) 
    
    emisora = []
    for i in range(N):
        emisora.append([fuente[i][0], filtrado[i][1]*moduladora[i][1]])
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(filtrado)
    datos[2] = conversor(moduladora)
    datos[3] = conversor(emisora)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_42():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5
    f0 = 1000
    
    onda_1     = gen_cod(Nd, Ts, Tb)
    onda_2     = convolve(onda_1, respuesta_filtro(N, a, Tb, Fs), 'same')
    moduladora = fuente(1.05*f0,Ts,0,N)     
    onda_3     = multiplicador(onda_2, moduladora)

    xi    = sqrt(2)/2   # Parámetros del PLL
    omega = 120
    K     = 1
    tipo  = 'rc'

    _, filtro, _, onda_4 = PLL(onda_3, tipo, xi, omega, f0, K, Ts)

    onda_5 = multiplicador(onda_2, onda_4)
    onda_6 = convolve(onda_5, 0.01*respuesta_filtro(1,200), 'same')    
    
    datos[0] = conversor(onda_3)
    datos[1] = conversor(filtro)
    datos[2] = conversor(onda_4)
    datos[3] = conversor(onda_6)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_43():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5
    f0 = 1000
    
    onda_1     = gen_cod(Nd, Ts, Tb)
    onda_2     = convolve(onda_1, respuesta_filtro(N, a, Tb, Fs), 'same')
    moduladora = fuente(1.05*f0,Ts,0,N)     
    onda_3     = multiplicador(onda_2, moduladora)

    xi    = sqrt(2)/2   # Parámetros del PLL
    omega = 220
    K     = 1
    tipo  = 'rc'

    _, filtro, _, onda_4 = PLL(onda_3, tipo, xi, omega, f0, K, Ts)

    onda_5 = multiplicador(onda_2, onda_4)
    onda_6 = convolve(onda_5, 0.01*respuesta_filtro(1,200), 'same')    
    
    datos[0] = conversor(onda_3)
    datos[1] = conversor(filtro)
    datos[2] = conversor(onda_4)
    datos[3] = conversor(onda_6)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_44():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5
    f0 = 1000
    
    """ Emisor """
    
    onda_1     = gen_cod(Nd, Ts, Tb)
    onda_2     = convolve(onda_1, respuesta_filtro(N, a, Tb, Fs), 'same')
    moduladora = fuente(1.05*f0,Ts,0,N)     
    onda_3     = multiplicador(onda_2, moduladora)

    xi    = sqrt(2)/2   # Parámetros del PLL
    omega = 450
    K     = 1
    tipo  = 'rc'

    """ Receptor """ 
    
    _, filtro, _, onda_4 = PLL(onda_3, tipo, xi, omega, f0, K, Ts)

    onda_5 = multiplicador(onda_2, onda_4)
    onda_6 = convolve(onda_5, 0.01*respuesta_filtro(1,200), 'same')    
    
    datos[0] = conversor(onda_3)
    datos[1] = conversor(filtro)
    datos[2] = conversor(onda_4)
    datos[3] = conversor(onda_6)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

def ejercicio_45():    
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5
    f0 = 1000
    
    """ Emisor """

    onda_1     = gen_cod(Nd, Ts, Tb)
    onda_2     = convolve(onda_1, respuesta_filtro(N, a, Tb, Fs), 'same')
    moduladora = fuente(1.05*f0,Ts,0,N)     
    onda_3     = multiplicador(onda_2, moduladora)

    xi    = sqrt(2)/2   # Parámetros del PLL
    omega = 120
    K     = 1
    tipo  = 'lead-lag activo'

    """ Receptor """
    
    _, filtro, _, onda_4 = PLL(onda_3, tipo, xi, omega, f0, K, Ts)

    onda_5 = multiplicador(onda_2, onda_4)
    onda_6 = convolve(onda_5, 0.01*respuesta_filtro(1,200), 'same')    
    
    datos[0] = conversor(onda_3)
    datos[1] = conversor(filtro)
    datos[2] = conversor(onda_4)
    datos[3] = conversor(onda_6)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], param 

"""
"Generar ahora una señal de entrada al PLL con el error de fase inicial de π/2, y un error de frecuencia del 10 %. Representar en cada caso la señal de error y el diagrama de Lissajous."
"""