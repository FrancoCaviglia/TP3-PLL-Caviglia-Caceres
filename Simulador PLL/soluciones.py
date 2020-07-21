# -*- coding: utf-8 -*-

import enunciados
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
from scipy import fftpack

#from nucleo import fuente as fuente

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
    
def ejercicio_1(ejercicio_enunciado, ejercicio_respuesta):
    
    datos = [0,0,0,0]
    
    datos[0] = conversor(fuente(10, 0.001, 0, 1000))
    datos[1] = conversor(fuente(10, 0.001, np.pi/2, 1000))
    datos[2] = conversor(fuente(5, 0.001, 0, 1000))
    datos[3] = conversor(fuente(5, 0.001, np.pi/2, 1000))
    
    ejercicio_enunciado["text"] = "Ejercicio 1. "+enunciados.enunciados[0]
    ejercicio_respuesta["text"] = enunciados.respuestas[0]
    
    return datos

def ejercicio_2(ejercicio_enunciado, ejercicio_respuesta):

    datos = [0,0,0,0]

    datos[0] = conversor(fuente(1000, 0.00001, np.pi/2, 1000))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    ejercicio_enunciado["text"] = "Ejercicio 2. "+enunciados.enunciados[1]
    ejercicio_respuesta["text"] = enunciados.respuestas[1]

    return datos

def ejercicio_3(ejercicio_enunciado, ejercicio_respuesta):
    
    datos = [0,0,0,0]

    datos[0] = conversor(unir_lista(fuente(1000, 0.00001, np.pi/2, 500), fuente(1000, 0.00001, 3*np.pi/2, 500)))
    datos[1] = [[],[]]
    datos[2] = [[],[]]
    datos[3] = [[],[]]
    
    ejercicio_enunciado["text"] = "Ejercicio 3. "+enunciados.enunciados[2]
    ejercicio_respuesta["text"] = enunciados.respuestas[2]

    return datos

def ejercicio_4(ejercicio_enunciado, ejercicio_respuesta):

    datos = [0,0,0,0]

    datos[0] = conversor(fuente(2000, 0.00001, np.pi/2, 1000))
    datos[1] = conversor(fuente(1000, 0.00001, 0, 1000))
    datos[2] = conversor(detector(fuente(1000, 0.00001, 0, 1000), fuente(3000, 0.00001, np.pi/2, 1000)))
    datos[3] = [[],[]]
    
    ejercicio_enunciado["text"] = "Ejercicio 4. "+enunciados.enunciados[3]
    ejercicio_respuesta["text"] = enunciados.respuestas[3]

    return datos

def ejercicio_5(ejercicio_enunciado, ejercicio_respuesta):

    datos = [0,0,0,0]

    datos[0] = conversor(fuente(1000, 0.00001, 0, 1000))
    datos[1] = conversor(fuente(1000, 0.00001, np.pi/4, 1000))
    datos[2] = conversor(detector(fuente(1000, 0.00001, 0, 1000), fuente(1000, 0.00001, np.pi/4, 1000)))
    datos[3] = [[],[]]
    
    ejercicio_enunciado["text"] = "Ejercicio 5. "+enunciados.enunciados[4]
    ejercicio_respuesta["text"] = enunciados.respuestas[4]
    
    return datos

def ejercicio_6(ejercicio_enunciado, ejercicio_respuesta):

    datos = [0,0,0,0]

    datos[0] = conversor(fuente(1000, 0.00001, 0, 1000))
    datos[1] = conversor(fuente(1000, 0.00001, np.pi/2, 1000))
    datos[2] = conversor(detector(fuente(1000, 0.00001, 0, 1000), fuente(1000, 0.00001, np.pi/2, 1000)))
    datos[3] = [[],[]]
    
    ejercicio_enunciado["text"] = "Ejercicio 6. "+enunciados.enunciados[5]
    ejercicio_respuesta["text"] = enunciados.respuestas[5]
    
    return datos

def ejercicio_7(ejercicio_enunciado, ejercicio_respuesta):
    
    entrada_1 = []
    entrada_2 = []
    
    for t in np.arange(-1,1,0.001):
        entrada_1.append([t, np.sin(2*np.pi*0.75*t*(1-t) + 2.1) + 0.1*np.sin(2*np.pi*1.25*t + 1) + 0.18*np.cos(2*np.pi*3.85*t) + np.random.random()*0.3])
        entrada_2.append([t, np.sin(2*np.pi*t) + 0.5*np.sin(2*np.pi*12*t)])
    
    salida_1 = filtro(entrada_1, None, 'rc', 0.25, 0.25, 0, 0.001)[0]
    salida_2 = filtro(entrada_2, None, 'rc', 0.25, 0.25, 0, 0.001)[0]

    datos = [0,0,0,0]

    datos[0] = conversor(entrada_1)
    datos[1] = conversor(salida_1)
    datos[2] = conversor(entrada_2)
    datos[3] = conversor(salida_2)
    
    ejercicio_enunciado["text"] = "Ejercicio 6. "+enunciados.enunciados[5]
    ejercicio_respuesta["text"] = enunciados.respuestas[5]
    
    return datos

def ejercicio_8(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 8. "+enunciados.enunciados[7]
    ejercicio_respuesta["text"] = enunciados.respuestas[7]
    
    return 0

def ejercicio_9(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 9. "+enunciados.enunciados[8]
    ejercicio_respuesta["text"] = enunciados.respuestas[8]
    
    return 0    

def ejercicio_10(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 10. "+enunciados.enunciados[9]
    ejercicio_respuesta["text"] = enunciados.respuestas[9]
    
    return 0

def ejercicio_11(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 11. "+enunciados.enunciados[10]
    ejercicio_respuesta["text"] = enunciados.respuestas[10]
    
    return 0    

def ejercicio_12(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 12. "+enunciados.enunciados[11]
    ejercicio_respuesta["text"] = enunciados.respuestas[11]
    
    return 0

def ejercicio_13(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 13. "+enunciados.enunciados[12]
    ejercicio_respuesta["text"] = enunciados.respuestas[12]
    
    return 0

def ejercicio_14(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 14. "+enunciados.enunciados[13]
    ejercicio_respuesta["text"] = enunciados.respuestas[13]
    
    return 0

def ejercicio_15(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 15. "+enunciados.enunciados[14]
    ejercicio_respuesta["text"] = enunciados.respuestas[14]
    
    return 0    

def ejercicio_16(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 16. "+enunciados.enunciados[15]
    ejercicio_respuesta["text"] = enunciados.respuestas[15]

    return 0

def ejercicio_17(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 17. "+enunciados.enunciados[16]
    ejercicio_respuesta["text"] = enunciados.respuestas[16]
    
    return 0

def ejercicio_18(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 18. "+enunciados.enunciados[17]
    ejercicio_respuesta["text"] = enunciados.respuestas[17]
    
    return 0

def ejercicio_19(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 19. "+enunciados.enunciados[18]
    ejercicio_respuesta["text"] = enunciados.respuestas[18]
    
    return 0

def ejercicio_20(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 20. "+enunciados.enunciados[19]
    ejercicio_respuesta["text"] = enunciados.respuestas[19]
    
    return 0

def ejercicio_21(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 21. "+enunciados.enunciados[20]
    ejercicio_respuesta["text"] = enunciados.respuestas[20]
 
    return 0

def ejercicio_22(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 22. "+enunciados.enunciados[21]
    ejercicio_respuesta["text"] = enunciados.respuestas[21]
 
    return 0    

def ejercicio_23(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 23. "+enunciados.enunciados[22]
    ejercicio_respuesta["text"] = enunciados.respuestas[22]
 
    return 0

def ejercicio_24(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 24. "+enunciados.enunciados[23]
    ejercicio_respuesta["text"] = enunciados.respuestas[23]
 
    return 0

def ejercicio_25(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 25. "+enunciados.enunciados[24]
    ejercicio_respuesta["text"] = enunciados.respuestas[24]
 
    return 0

def ejercicio_26(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 26. "+enunciados.enunciados[25]
    ejercicio_respuesta["text"] = enunciados.respuestas[25]
 
    return 0

def ejercicio_27(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 27. "+enunciados.enunciados[26]
    ejercicio_respuesta["text"] = enunciados.respuestas[26]
 
    return 0

def ejercicio_28(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 28. "+enunciados.enunciados[27]
    ejercicio_respuesta["text"] = enunciados.respuestas[27]
 
    return 0    

def ejercicio_29(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 29. "+enunciados.enunciados[28]
    ejercicio_respuesta["text"] = enunciados.respuestas[28]
 
    return 0

def ejercicio_30(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 30. "+enunciados.enunciados[29]
    ejercicio_respuesta["text"] = enunciados.respuestas[29]
 
    return 0

def ejercicio_31(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 31. "+enunciados.enunciados[30]
    ejercicio_respuesta["text"] = enunciados.respuestas[30]
 
    return 0

def ejercicio_32(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 32. "+enunciados.enunciados[31]
    ejercicio_respuesta["text"] = enunciados.respuestas[31]
 
    return 0

def ejercicio_33(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 33. "+enunciados.enunciados[32]
    ejercicio_respuesta["text"] = enunciados.respuestas[32]
 
    return 0

def ejercicio_34(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 34. "+enunciados.enunciados[33]
    ejercicio_respuesta["text"] = enunciados.respuestas[33]
 
    return 0

def ejercicio_35(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 35. "+enunciados.enunciados[34]
    ejercicio_respuesta["text"] = enunciados.respuestas[34]
     
    return 0

def ejercicio_36(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 36. "+enunciados.enunciados[35]
    ejercicio_respuesta["text"] = enunciados.respuestas[35]

    return 0    

def ejercicio_37(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 37. "+enunciados.enunciados[36]
    ejercicio_respuesta["text"] = enunciados.respuestas[36]
 
    return 0

def ejercicio_38(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 38. "+enunciados.enunciados[37]
    ejercicio_respuesta["text"] = enunciados.respuestas[37]
 
    return 0

def ejercicio_39(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 39. "+enunciados.enunciados[38]
    ejercicio_respuesta["text"] = enunciados.respuestas[38]
 
    return 0    

def ejercicio_40(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 40. "+enunciados.enunciados[39]
    ejercicio_respuesta["text"] = enunciados.respuestas[39]
 
    return 0

def ejercicio_41(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 41. "+enunciados.enunciados[40]
    ejercicio_respuesta["text"] = enunciados.respuestas[40]

    return 0

def ejercicio_42(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 42. "+enunciados.enunciados[41]
    ejercicio_respuesta["text"] = enunciados.respuestas[41]
 
    return 0

def ejercicio_43(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 43. "+enunciados.enunciados[42]
    ejercicio_respuesta["text"] = enunciados.respuestas[42]
 
    return 0    

def ejercicio_44(ejercicio_enunciado, ejercicio_respuesta):

    ejercicio_enunciado["text"] = "Ejercicio 44. "+enunciados.enunciados[43]
    ejercicio_respuesta["text"] = enunciados.respuestas[43]
 
    return 0    

def ejercicio_45(ejercicio_enunciado, ejercicio_respuesta):    

    ejercicio_enunciado["text"] = "Ejercicio 45. "+enunciados.enunciados[44]
    ejercicio_respuesta["text"] = enunciados.respuestas[44]
     
    return 0

"""
"Generar ahora una señal de entrada al PLL con el error de fase inicial de π/2, y un error de frecuencia del 10 %. Representar en cada caso la señal de error y el diagrama de Lissajous."
"""