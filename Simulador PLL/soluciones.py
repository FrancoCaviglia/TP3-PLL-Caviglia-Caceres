# -*- coding: utf-8 -*-

"""

Revisado por última vez el Viernes 7 de Agosto a las 22:00 2020.
@author: Franco Caviglia, Joan Joel Cáceres

"""

from auxiliar import *

""" En este archivo se encuentran las 45 funciones con nombre ejercicio_X que se corresponden con cada
    uno de los 45 ejercicios de la guía. Para funcionar utilizan las funciones construidas en auxiliar.py.
    Como retorno devuelven los datos necesarios para mostrar los resultados en la interfaz (GUI). En caso
    de que el ejercicio sólo implique construir una función, se muestra un ejemplo de su aplicación. Cada
    función tiene la misma estructura: primero los parámetros necesarios, luego el armado de los datos para
    las gráficas, luego se pasan esos datos a la lista "datos" y finalmente se retornan en orden dicha lista,
    las leyendas, y los parámetros usados.
"""

datos = [ [[],[]], [[],[]], [[],[]], [[],[]], [[],[]], [[],[]] ]
param = ['', '', '', '', '', '', '', '', '', '', '', '']
leyendas = ['Tiempo (s)', 'Amplitud (V)']

def ejercicio_1():
    
    datos[0] = conversor(fuente(10, 0.001,    0, 1000))
    datos[1] = conversor(fuente(10, 0.001, pi/2, 1000))
    datos[2] = conversor(fuente(5,  0.001,    0, 1000))
    datos[3] = conversor(fuente(5,  0.001, pi/2, 1000))
    datos[4] = conversor(fuente(1,  0.001,    0, 1000))
    datos[5] = conversor(fuente(1,  0.001, pi/2, 1000))
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [1000, 1000, '10, 5', '0, π/2', '', '', '', '', '', '', '','']

def ejercicio_2():
    
    N  = 1000
    f0 = 1000
    fs = 100*f0
    Ts = 1/fs
    
    datos[0] = conversor(fuente(f0, Ts, pi/2, N))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'],  [N, fs, f0, 'π/2', '', '', '', '', '', '', '','']

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
    datos[4] = [[],[]]
    datos[5] = [[],[]]   

    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, 'π/2', '', '', '', '', '', '', '','']

def ejercicio_4():

    entrada_1 = fuente(100, 0.00001, 0, 1000)
    entrada_2 = fuente(200, 0.00001, pi/2, 1000)
    
    datos[0] = conversor(entrada_1)
    datos[1] = conversor(entrada_2)
    datos[2] = conversor(detector(entrada_1, entrada_2))
    datos[3] = [[],[]]
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [1000, 100000, '100, 200', '0, π/2', '', '', '', '', '', '', '','']

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
    datos[4] = [[],[]]
    datos[5] = [[],[]]
      
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, 1/Ts, f0, '0, π/4', '', '', '', '', '', '', '','']

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
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, 1/Ts, f0, '0, π/2', '', '', '', '', '', '', '','']

def ejercicio_7():
    
    N  = 2000
    Ts = 0.001
    zi = []
    
    entrada_1 = []
    entrada_2 = []
    
    for t in arange(-1,1,Ts):
        entrada_1.append([t, sin(2*pi*0.75*t*(1-t) + 2.1) + 0.1*sin(2*pi*1.25*t + 1) + 0.18*cos(2*pi*3.85*t) + random()*0.3])
        entrada_2.append([t, sin(2*pi*t) + 0.5*sin(2*pi*12*t)])
    
    salida_1 = filtro(entrada_1, zi, 'rc', 0.25, 0.25, 0, Ts)[0]
    salida_2 = filtro(entrada_1, zi, 'lead-lag activo', 0.25, 0.25, 0.25, Ts)[0]
    salida_3 = filtro(entrada_2, zi, 'rc', 0.25, 0.25, 0, Ts)[0]
    salida_4 = filtro(entrada_2, zi, 'lead-lag activo', 0.25, 0.25, 0.25, Ts)[0]

    datos[0] = conversor(entrada_1)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(salida_2)
    datos[3] = conversor(entrada_2)
    datos[4] = conversor(salida_3)
    datos[5] = conversor(salida_4)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, 1/Ts, '', '', '', '', '', '', '', 'rc', '', '']

def ejercicio_8():
    
    Ts = 0.00001
    N  = 10000000
    zi = []
    tipo = 'rc'
    
    entrada = delta_0(1, 0.0001, N, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(filtro_traducido(entrada, zi, tipo,   2, sqrt(2)/2, Ts)[0])
    datos[2] = conversor(filtro_traducido(entrada, zi, tipo, 100, sqrt(2)/2, Ts)[0])
    datos[3] = conversor(filtro_traducido(entrada, zi, tipo,   2,         5, Ts)[0])
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, int(1/Ts), '', '', '√2/2, √2/2, 5', '2, 100, 2', '', '', '', tipo, '', '']

def ejercicio_9():
    
    N  = 2000                   # Cantidad de muestras
    f  = 1000                   # Frecuencia de la portadora
    Ts = 1/(100*f)              # Período de muestreo
    zi = []                     # Condiciones iniciales para el filtro
    tipo = 'rc'                 # Tipo de filtro
    
    entrada_1 = fuente(f, Ts, 0, N)
    entrada_2 = fuente(f, Ts, pi/4, N)
    salida_detector = detector(entrada_1, entrada_2)
    
    datos[0] = conversor(entrada_1)
    datos[1] = conversor(entrada_2)
    datos[2] = conversor(salida_detector)
    datos[3] = conversor(filtro_traducido(salida_detector, zi, tipo,   2, sqrt(2)/2, Ts)[0])
    datos[4] = conversor(filtro_traducido(salida_detector, zi, tipo, 100, sqrt(2)/2, Ts)[0])
    datos[5] = conversor(filtro_traducido(salida_detector, zi, tipo,   2,         5, Ts)[0])
        
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, int(1/Ts), f, '0, π/4', '√2/2, √2/2, 5', '2, 100, 2', '', '', '', tipo, '', '']

def ejercicio_10():

    N  = 2000                   # Cantidad de muestras
    f  = 1000                   # Frecuencia de la portadora
    Ts = 1/(100*f)              # Período de muestreo
    zi = []                     # Condiciones iniciales para el filtro
    tipo = 'lead-lag activo'    # Tipo de filtro

    entrada_1 = fuente(f, Ts, 0, N)
    entrada_2 = fuente(f, Ts, pi/4, N)
    salida_detector = detector(entrada_1, entrada_2)
    
    datos[0] = conversor(entrada_1)
    datos[1] = conversor(entrada_2)
    datos[2] = conversor(salida_detector)
    datos[3] = conversor(filtro_traducido(salida_detector, zi, tipo,   2, sqrt(2)/2, Ts)[0])
    datos[4] = conversor(filtro_traducido(salida_detector, zi, tipo, 100, sqrt(2)/2, Ts)[0])
    datos[5] = conversor(filtro_traducido(salida_detector, zi, tipo,   2,       0.1, Ts)[0])
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [2000, 100000, 1000, '0, π/4', '√ 2/2, √ 2/2, 0.1', '2, 100, 2', '', '', '', 'll activo', '', '']

def ejercicio_11():

    Ts = 0.001
    N  = 1000
    K  = 1
    f0 = 1000
    
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
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Fase VCO'], [N, int(1/Ts), '10, 5', '0', '', '', '', K, '', '', '', '']

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
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, fase_inicial, '', '', '', '', '', '', '', '']

def ejercicio_13():

    N  = 1000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fmod = 40                   # Frecuencia de la señal moduladora (o de control)
    fs = 10*f0                  # Frecuencia de muestro
    fase_inicial = 0
    Ts = 1/fs                   # Período de muestreo
    K  = 0
    ph = 0                      # Fase inicial de la salida del VCO

    onda_mod = fuente(fmod, Ts, fase_inicial, N) # Fabrica la onda moduladora              
    
    salida_mod = vco(onda_mod, Ts, K, f0, ph)[0] #Pasa la onda moduladora por un VCO con K=0

    datos[0] = conversor(onda_mod)
    datos[1] = conversor(salida_mod)             #conversor(fourier(onda_mod, Ts))
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, fmod, fase_inicial, '', '', '', K, f0, '', '', '']

def ejercicio_14():
    
    N  = 1000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fmod = 40                   # Frecuencia de la señal moduladora (o de control)
    fs = 10*f0                  # Frecuencia de muestro
    fase_inicial = 0
    Ts = 1/fs                   # Período de muestreo
    K  = 100                    # Ganancia de lazo
    ph = 0                      # Fase inicial de la salida del VCO
    
    onda_mod = fuente(fmod, Ts, fase_inicial, N) # Fabrica la onda moduladora              
    
    salida_mod = vco(onda_mod, Ts, K, f0, ph)[0] # Pasa la onda moduladora por un VCO con K = 100
    
    datos[0] = conversor(onda_mod)
    datos[1] = conversor(salida_mod)
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, fmod, fase_inicial, '', '', '', K, f0, '', '', '']

def ejercicio_15():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Pulsación propia
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    
    _, salida_1, _, _, K1 = PLL(entrada, 'rc', sqrt(2)/2, wn, f0, Ts)
    _, salida_2, _, _, K2 = PLL(entrada, 'rc',       0.3, wn, f0, Ts)
    _, salida_3, _, _, K3 = PLL(entrada, 'rc',       2.0, wn, f0, Ts)

    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(salida_2)
    datos[3] = conversor(salida_3)
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', '', '', '', f'{K1}, {K2}, {K3}', f0, 'rc', '', '']

def ejercicio_16():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    _, error_1, _, salida_1, K1 = PLL(entrada, 'rc', sqrt(2)/2, wn, f0, Ts)
    _, error_2, _, salida_2, K2 = PLL(entrada, 'rc',       0.3, wn, f0, Ts)
    _, error_3, _, salida_3, K3 = PLL(entrada, 'rc',         2, wn, f0, Ts)
    
    datos[0] = lissajous(entrada, salida_1)
    datos[1] = error(entrada, salida_1)
    datos[2] = lissajous(entrada, salida_2)
    datos[3] = error(entrada, salida_2)
    datos[4] = lissajous(entrada, salida_3)
    datos[5] = error(entrada, salida_3)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'],  [N, fs, f0, '', '', '', '', f'{K1}, {K2}, {K3}', f0, 'rc', '', '']

def ejercicio_17():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 120
    xi = sqrt(2)/2
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    _, _, salida_filtro, salida_vco, K = PLL(entrada, 'rc', xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, wn, '', K, f0, 'rc', '', '']

def ejercicio_18():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 40
    xi = sqrt(2)/2
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    _, _, salida_filtro, salida_vco, K = PLL(entrada, 'lead-lag activo', xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, wn, '', K, f0, 'rc', '', '']

def ejercicio_19():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 120
    xi = sqrt(2)/2
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/2, N//2))
    _, _, salida_filtro, salida_vco, K = PLL(entrada, 'lead-lag activo', xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = [[],[]]
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, wn, '', K, f0, 'll activo', '', '']

def ejercicio_20():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 220
    xi = 2
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/4, N//2))
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, wn, '', K, f0, tipo, '', '']

def ejercicio_21():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 220
    xi = sqrt(2)/2
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/4, N//2))
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, wn, '', K, f0, tipo, '', '']

def ejercicio_22():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 80
    xi = sqrt(2)/2
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/4, N//2))
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, wn, '', K, f0, 'll activo', '', '']

def ejercicio_23():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'lead-lag activo'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, pi/4, N//2))
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'],  [N, fs, f0, '', xi, wn, '', K, f0, 'll activo', '', '']

def ejercicio_24():
  
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = f0                     # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 220                    # Parámetros de los filtros
    xi = 2
    tipo = 'rc'
    
    entrada  = unir_lista(fuente(f, Ts, 0, N//2), fuente(f, Ts, error_fase, N//2))
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, wn, '', K, f0, tipo, '', '']

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
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, wn, '', K, f0, 'll activo', '', '']

def ejercicio_26():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'rc'
    
    entrada = fuente(f, Ts, error_fase, N)
    _, salida_detector, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_detector)
    datos[2] = conversor(salida_filtro)
    datos[3] = conversor(salida_vco)
    datos[4] = lissajous(entrada, salida_vco)
    datos[5] = error(entrada, salida_vco)
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f, '', xi, wn, '', K, f0, 'll activo', '', '']

def ejercicio_27():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 450                    # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'rc'
    
    entrada  = fuente(f, Ts, error_fase, N//2)
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f, '', xi, wn, '', K, f0, tipo, '', '']

def ejercicio_28():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 450                    # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'rc'
    
    entrada = fuente(f, Ts, error_fase, N//2)
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f, '', xi, wn, '', K, f0, tipo, '', '']

def ejercicio_29():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'lead-lag activo'
    
    entrada = fuente(f, Ts, error_fase, N//2)
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f, '', xi, wn, '', K, f0, 'll activo', '', '']

def ejercicio_30():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 120                    # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'lead-lag activo'
    
    entrada = fuente(f, Ts, error_fase, N//2)
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f, '', xi, wn, '', K, f0, 'll activo', '', '']

def ejercicio_31():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.1*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 80                     # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'lead-lag activo'
    
    entrada = fuente(f, Ts, error_fase, N//2)
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f, '', xi, wn, '', K, f0, 'll activo', '', '']

def ejercicio_32():

    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    f  = 1.03*f0                 # Frecuencia de entrada
    error_fase = pi
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 80                     # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'lead-lag activo'
    
    entrada = fuente(f, Ts, error_fase, N//2)
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f, '', xi, wn, '', K, f0, 'll activo', '', '']

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
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, 1/Ts, '1000 a 1100', 0, '', '', '', '', '', '', '', '']

def ejercicio_34():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fase_inicial = pi/2
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 450                    # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'rc'
    
    entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, 1100, fase_inicial, xi, wn, '', K, f0, tipo, '', '']

def ejercicio_35():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fase_inicial = pi/2
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 180                    # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'lead-lag activo'
    
    entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, 1100, fase_inicial, xi, wn, '', K, f0, 'll activo', '', '']

def ejercicio_36():
    
    N  = 3000                   # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fase_inicial = pi/2
    fs = 100*f0                 # Frecuencia de muestro
    Ts = 1/fs                   # Período de muestreo
    wn = 280                    # Parámetros de los filtros
    xi = sqrt(2)/2
    tipo = 'lead-lag activo'
    
    entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)
    _, _, salida_filtro, salida_vco, K = PLL(entrada, tipo, xi, wn, f0, Ts)
    
    datos[0] = conversor(entrada)
    datos[1] = conversor(salida_filtro)
    datos[2] = conversor(salida_vco)
    datos[3] = lissajous(entrada, salida_vco)
    datos[4] = error(entrada, salida_vco)
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, 1100, fase_inicial, xi, wn, '', K, f0, 'll activo', '', '']

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
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, 0.5, '', '', '', Tb, '', '', '', '', Nd]

def ejercicio_38():

    Fs = 1
    a  = 0.5
    N  = 100
    Tb = 2

    datos[0] = conversor(respuesta_filtro(N, a, Tb, Fs))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, '', '', '', '', '', Tb, '', '', '', a, '']

def ejercicio_39():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5        # Factor de roll-off

    entrada = conversor(gen_cod(Nd, Ts, Tb))
    salida  = convolve(entrada[1], respuesta_filtro(N, a, Tb, Fs)[1], 'same')
    
    datos[0] = entrada
    datos[1] = [entrada[0], salida]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, '', '', '', '', Tb, '', '', '', a, Nd]

def ejercicio_40():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 1          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5

    entrada = conversor(gen_cod(Nd, Ts, Tb))
    salida  = convolve(entrada[1], respuesta_filtro(N, a, Tb, Fs)[1], 'same')
    
    datos[0] = entrada
    datos[1] = [entrada[0], salida]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, '', '', '', '', Tb, '', '', '', a, Nd] 

def ejercicio_41():
    
    Nd = 10         # Cantidad de pulsos
    fs = 20000      # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 0.5
    f0 = 1000
    
    entrada    = conversor(gen_cod(Nd, Ts, Tb))
    filtrado   = convolve(entrada[1], rcosfilter(N, a, Tb, 20)[1], 'same')
    portadora  = fuente(f0,Ts,0,N) 

    emisora = []
    for i in range(N):
        emisora.append([portadora[i][0], filtrado[i]*portadora[i][1]])
    
    datos[0] = entrada
    datos[1] = [entrada[0], filtrado]
    datos[2] = conversor(portadora)
    datos[3] = conversor(emisora)
    datos[4] = [[],[]]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, '', '', '', '', Tb, '', '', '', a, Nd] 

def ejercicio_42():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 1          # Factor roll-off
    f0 = 1000
    
    onda_1     = conversor(gen_cod(Nd, Ts, Tb))
    onda_2     = [onda_1[0] , convolve(onda_1[1], rcosfilter(N, a, 2, Fs)[1], 'same')]
    moduladora = fuente(1.05*f0,Ts,0,N)     
    onda_3     = []
    for i in range(len(moduladora)):
        onda_3.append([onda_2[0][i], onda_2[1][i]*moduladora[i][1]])
        
    xi    = sqrt(2)/2   # Parámetros del PLL
    omega = 120
    K     = 1
    tipo  = 'rc'
    
    a = 1

    _, filtro, _, onda_4, K = PLL(onda_3, tipo, xi, omega, f0, Ts)

    onda_5 = []
    del onda_4[0]
    for i in range(len(onda_4)):
        onda_5.append([onda_3[i][0], onda_3[i][1]*onda_4[i][1]])
    
    onda_6 = convolve(conversor(onda_5)[1], 0.01*rcosfilter(N, a, 2, Fs)[1], 'same')    
    
    datos[0] = onda_1
    datos[1] = conversor(onda_3)
    datos[2] = conversor(filtro)
    datos[3] = conversor(onda_4)
    datos[4] = [conversor(onda_5)[1], onda_6]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, omega, Tb, K, f0, tipo, a, Nd]

def ejercicio_43():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 1
    f0 = 1000
    
    onda_1     = conversor(gen_cod(Nd, Ts, Tb))
    onda_2     = [onda_1[0] , convolve(onda_1[1], rcosfilter(N, a, 2, 30)[1], 'same')]
    moduladora = fuente(1.05*f0,Ts,0,N)     
    onda_3     = []
    for i in range(len(moduladora)):
        onda_3.append([onda_2[0][i], onda_2[1][i]*moduladora[i][1]])
        
    xi    = sqrt(2)/2   # Parámetros del PLL
    omega = 220
    K     = 1
    tipo  = 'rc'

    _, filtro, _, onda_4, K = PLL(onda_3, tipo, xi, omega, f0, Ts)

    onda_5 = []
    del onda_4[0]
    for i in range(len(onda_4)):
        onda_5.append([onda_3[i][0], onda_3[i][1]*onda_4[i][1]])
    
    onda_6 = convolve(conversor(onda_5)[1], 0.01*rcosfilter(N, a, 2, Fs)[1], 'same')    

    datos[0] = onda_1    
    datos[1] = conversor(onda_3)
    datos[2] = conversor(filtro)
    datos[3] = conversor(onda_4)
    datos[4] = [conversor(onda_5)[1], onda_6]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, omega, Tb, K, f0, tipo, a, Nd]

def ejercicio_44():
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 1
    f0 = 1000
    
    """ Emisor """
    
    onda_1     = conversor(gen_cod(Nd, Ts, Tb))
    onda_2     = [onda_1[0] , convolve(onda_1[1], rcosfilter(N, a, 2, 30)[1], 'same')]
    moduladora = fuente(1.05*f0,Ts,0,N)     
    onda_3     = []
    for i in range(len(moduladora)):
        onda_3.append([onda_2[0][i], onda_2[1][i]*moduladora[i][1]])
        
    xi    = sqrt(2)/2   # Parámetros del PLL
    omega = 450
    tipo  = 'rc'

    """ Receptor """ 

    _, filtro, _, onda_4, K = PLL(onda_3, tipo, xi, omega, f0, Ts)

    onda_5 = []
    del onda_4[0]
    for i in range(len(onda_4)):
        onda_5.append([onda_3[i][0], onda_3[i][1]*onda_4[i][1]])
    
    onda_6 = convolve(conversor(onda_5)[1], 0.01*rcosfilter(N, a, 2, Fs)[1], 'same')    
    
    datos[0] = onda_1    
    datos[1] = conversor(onda_3)
    datos[2] = conversor(filtro)
    datos[3] = conversor(onda_4)
    datos[4] = [conversor(onda_5)[1], onda_6]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, omega, Tb, K, f0, tipo, a, Nd]  

def ejercicio_45():    
    
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras
    Fs = 1
    a  = 1          # Factor de roll off
    f0 = 1000
    
    """ Emisor """
    
    onda_1     = conversor(gen_cod(Nd, Ts, Tb))
    onda_2     = [onda_1[0] , convolve(onda_1[1], rcosfilter(N, a, 2, 30)[1], 'same')]
    moduladora = fuente(1.05*f0,Ts,0,N)     
    onda_3     = []
    for i in range(len(moduladora)):
        onda_3.append([onda_2[0][i], onda_2[1][i]*moduladora[i][1]])
        
    xi    = sqrt(2)/2   # Parámetros del PLL
    omega = 120
    K     = 1
    tipo  = 'lead-lag activo'

    """ Receptor """ 

    _, filtro, _, onda_4, K = PLL(onda_3, tipo, xi, omega, f0, Ts)

    onda_5 = []
    del onda_4[0]
    for i in range(len(onda_4)):
        onda_5.append([onda_3[i][0], onda_3[i][1]*onda_4[i][1]])
    
    onda_6 = convolve(conversor(onda_5)[1], 0.01*rcosfilter(N, a, 2, Fs)[1], 'same')    
    
    datos[0] = onda_1    
    datos[1] = conversor(onda_3)
    datos[2] = conversor(filtro)
    datos[3] = conversor(onda_4)
    datos[4] = [conversor(onda_5)[1], onda_6]
    datos[5] = [[],[]]
    
    return datos, ['Tiempo (s)', 'Amplitud (V)'], [N, fs, f0, '', xi, omega, Tb, K, f0, 'll activo', a, Nd]