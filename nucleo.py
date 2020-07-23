import time

# Apéndice

def suma_lista(v,w):
    suma = []
    for i in range(len(v)):
        suma.append([v[i][0],v[i][1]+w[i][1]])

    return suma

# Transformada de Fourier

def fourier(v,Ts):

    entrada = []
    salida = []

    for elem in v:
        entrada.append(elem[1])

    yfreq = fftpack.fft(entrada)    #
    yfreq = fftpack.fftshift(yfreq) # Ordena el vector yfreq para poder usarlo

    xfreq = fftpack.fftfreq(len(v),Ts)
    xfreq = fftpack.fftshift(xfreq)

    for i in range(len(entrada)):          # Fabrica los pares (x,y)
        salida.append([xfreq[i], np.abs(yfreq[i])]) # Puede tomar parte real o imaginaria

    return salida

# Gráficas en Latex

def graficar(v, leyenda_x='x', leyenda_y='y', encabezado='Grafica', nombre_archivo='untitle', referencia='Tension'):
    
    x = []
    y = []
    
    for i in range(len(v)):
        x.append(v[i][0])
        y.append(v[i][1])
         
    # use LaTeX fonts in the plot
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
     
    f = plt.figure()
    
    # plot
    plt.plot(x, y, label=referencia)
#   set labels (LaTeX can be used)
    plt.title(r'\textbf{'+leyenda_y+'}', fontsize=11)
    plt.xlabel(r'\textbf{'+leyenda_x+'}', fontsize=11)
    plt.ylabel(r'\textbf{'+encabezado+'}', fontsize=11)
#   plt.margins(0,0.05)
    plt.grid()
#   plt.legend()
    plt.show()
    
    #f.savefig(nombre_archivo+".pdf", bbox_inches='tight')
    
#    plt.title(r'$A \times B$')
#    plt.savefig('test.png')

# Diagrama de Lissajous

def lissajous(v,w):
    
    salida = []
    for i in range(len(v)):
        salida.append([v[i][1],w[i][1]])
    
    return salida

def graficar_lissajous(v,w):
    entrada = lissajous(v,w)
    graficar(entrada, 'Tension (V)', 'Tension (V)', 'Diagrama de Lissajous', 'lissajous')
    
    return 0

def graficar_error(v,w):
    entrada = []
    for i in range(len(v)):
        entrada.append([v[i][0],v[i][1]+w[i][1]])
    graficar(entrada, 'Tension (V)', 'Tension (V)', 'Diagrama de Lissajous', 'lissajous')
    
    return 0

# 3. Detector de fases

def detector(xr, xv, K=1): 
    
    producto = []
    
    for i in range(len(xr)):
        producto.append([xr[i][0],K*xr[i][1]*xv[i][1]])
        
    return producto

def ejercicio_6():

    f0 = 1000
    Ts = 1/(100*f0)
    fase_1 = 0
    fase_2 = np.pi/2
    
    onda_1 = fuente(f0, Ts, fase_1, 1000)
    onda_2 = fuente(f0, Ts, fase_2, 1000)

    resultado = detector(onda_1,onda_2)

    graficar(resultado, 'Tiempo (t)', 'Amplitud (V)', 'Ejercicio 5')
    graficar(fourier(resultado, Ts), 'Frecuencia (Hz)', 'Amplitud (V)', 'Ejercicio 5')
  
    return 0

# 4. Filtro

# Ejercicio 7

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

# Traductor parámetros

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
# Aproximantes de la delta

def delta_0(m, t0, N, Ts):

    salida = [ ]

    for t in np.arange(0,N*Ts,Ts):
        if t == t0:
            salida.append([t,m])
        else:
            salida.append([t,0])
            
    return salida

def delta_1(m, t0, N, Ts):

    salida = [ ]
    t = 0

    for i in range(N):
        salida.append([t, np.sin(m*(t-t0))/(np.pi*(t-t0))])
        t+=Ts
    return salida

def delta_2(m, t0, N, Ts):

    salida = [ ]
    t = 0
    spi = np.sqrt(np.pi)

    for i in range(N):
        salida.append([t, m*np.exp(-(m*(t-t0))**2)/spi])
        t+=Ts
    return salida

def delta_3(e, t0, N, Ts):

    salida = [ ]
    t = 0
    inv_pi = e/np.pi

    for i in range(N):
        salida.append([t,inv_pi/(t**2+e**2)])
        t+=Ts
    return salida

def delta_5(m,L,N,Ts):

    salida = [ ]
    t = 0
  
    for i in range(N):
        valor = 1/(2*L)
        for j in range(m):
              valor += np.cos(j*np.pi*t/L)
        salida.append([t,valor])
        t += Ts

    return salida

def delta_6(t0,N):
    salida = sc.signal.unit_impulse(N,t0)
    return salida

def ejercicio_8():
    
    Ts = 0.0001
    N = 1000
    estado_inicial = [0,0]
    test1=  filtro_traducido(delta_1(10, 10, N, Ts),estado_inicial, 'rc', np.sqrt(2)/2, 2, Ts)
    test2=  filtro_traducido(delta_1(10, 10, N, Ts),estado_inicial, 'rc', np.sqrt(2)/2, 100, Ts)
    test3=  filtro_traducido(delta_1(10, 10, N, Ts),estado_inicial, 'rc', 5, 2, Ts)
    
    graficar(test1, 'Tiempo (t)', 'Amplitud (V)','Ejercicio 8')
    graficar(test2, 'Tiempo (t)', 'Amplitud (V)','Ejercicio 8')
    graficar(test3, 'Tiempo (t)', 'Amplitud (V)','Ejercicio 8')
    
    graficar(fourier(test1), 'Tiempo (t)', 'Amplitud (V)','Ejercicio 8')
    graficar(fourier(test2), 'Tiempo (t)', 'Amplitud (V)','Ejercicio 8')
    graficar(fourier(test3), 'Tiempo (t)', 'Amplitud (V)','Ejercicio 8')

def ejercicio_9():

    N = 2000
    f0 = 1000
    ts = 0.001
    
    fase_1 = 0
    fase_2 = np.pi/4
    
    onda_1 = fuente(f0, Ts, fase_1, N)
    onda_2 = fuente(f0, Ts, fase_2, N)

    onda_3 = detector(onda_1, onda_2)

    for param in [[np.sqrt(2)/2, 2], [np.sqrt(2)/2, 100], [5, 2]]:    # Itera sobre los pares de parámetros que se piden
        
        resultado = filtro_traducido(onda_3,[0,0], 'rc', param[0], param[1], Ts)
        graficar(resultado, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
        graficar(fourier(resultado, Ts), 'Frecuencia (Hz)', 'Amplitud (V)', 'FFT')
    
    return 0

def ejercicio_10():

    N = 2000
    f0 = 1000
    Ts = 1/(100*f0)

    fase_1 = 0
    fase_2 = np.pi/4
    
    onda_1 = fuente(f0, Ts, fase_1, N)
    onda_2 = fuente(f0, Ts, fase_2, N)

    onda_3 = detector(onda_1, onda_2)

    for param in [[np.sqrt(2)/2, 2], [np.sqrt(2)/2, 100], [0.1, 2]]:    # Itera sobre los pares de parámetros que se piden

        resultado = filtro_traducido(onda_3,[0,0], 'lead-lag activo', param[0], param[1], Ts)
        graficar(resultado, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
        graficar(fourier(resultado,Ts), 'Frecuencia (Hz)', 'Amplitud (V)', 'FFT')

    return 0

# 5. Oscilador Controlado por Voltaje (VCO)

# Ejercicio 11

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

def ejercicios_12_a_14():
    
    N = 1000                    # Númerto total de muestras
    f0 = 1000                   # Frecuencia central de oscilación del VCO
    fmod = 40                   # Frecuencia de la señal moduladora (o de control)
    fs = 10*f0                  # Frecuencia de muestro
    fase_inicial = 0
    Ts = 1/fs                   # Período de muestreo
    
    onda_mod = fuente(fmod, Ts, fase_inicial, N)                        # Fabrica la onda moduladora
    
    graficar(onda_mod, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar(fourier(onda_mod, Ts), 'Frecuencia (Hz)', 'Amplitud (V)', 'FFT')
    
    for i in [0,1000]:
        salida_mod = vco(onda_mod, Ts, i, f0)                           # Pasa la onda moduladora por un VCO con K=0
    
    graficar(salida_mod, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar(fourier(salida_mod, Ts), 'Frecuencia (Hz)', 'Amplitud (V)', 'FFT')

# 6. Lazo Enganchado en Fase

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

def cosas():
    f0 = 1000
    fase_inicial = np.pi/2
    N = 3000
    f_muestreo = 100*f0
    Ts = 1/f_muestreo
    estado_inicial = [0,0]
    
    onda_entrada = fuente(f0,Ts,fase_inicial, N)

    for xi in [np.sqrt(2)/2, 0.3, 2.0]:
        onda_salida = filtro_traducido(onda_entrada, estado_inicial, 'rc', xi, 180)
        graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
        graficar_lissajous(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
        graficar_error(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Error señal')

def ejercicio_17():

    onda_salida = filtro_traducido(onda_entrada, estado_inicial, 'rc', np.sqrt(2)/2, 120, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_error(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Error señal')

def ejercicio_18():

    onda_salida = PLL(onda_entrada, 'lead-lag activo', estado_inicial, np.sqrt(2)/2, 40, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_error(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Error señal')

def ejercicio_19():

    onda_salida  = PLL(onda_entrada, 'lead-lag activo', estado_inicial, np.sqrt(2)/2, 120, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_error(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Error señal')


# 6.1 Errores de fase

onda_error  = fuente(f0,Ts,fase_inicial, N//2) + fuente(f0,Ts,fase_inicial + np.pi/4, N//2)


def ejercicio_20():

    f0 = 1000
    fase_inicial = np.pi/2
    N = 3000
    f_muestreo = 100*f0
    Ts = 1/f_muestreo
    K= 1 # no hay un valor definido de él para este inciso.

    onda_salida = PLL(onda_error, 'rc', 2, 220, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_error(onda_entrada, onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Error señal')

    return 0

def ejercicio_21():

    f0 = 1000
    fase_inicial = np.pi/2
    N = 3000
    f_muestreo = 100*f0
    Ts = 1/f_muestreo
    K = 1 # no hay un valor definido de él para este inciso.

    onda_salida = PLL(onda_error, 'rc', np.sqrt(2)/2, 220, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)
    graficar_error(onda_entrada, onda_salida)

    return 0

def ejercicio_22():

    f0 = 1000
    fase_inicial = np.pi/2
    N = 3000
    f_muestreo = 100*f0
    Ts = 1/f_muestreo
    K = 1 #no hay un valor definido de él para este inciso.

    onda_salida = PLL(onda_error, 'lead-lag activo', np.sqrt(2)/2, 220, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)
    graficar_error(onda_entrada, onda_salida)

    return 0

def ejercicio_23():

    f0 = 1000
    fase_inicial = np.pi/2
    N = 3000
    f_muestreo = 100*f0
    Ts = 1/f_muestreo
    K= 1 #no hay un valor definido de él para este inciso.
  
    onda_salida = PLL(onda_error, 'rc', np.sqrt(2)/2, 180, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)
    graficar_error(onda_entrada, onda_salida)

    return 0

#onda_error  = fuente(f0,Ts,fase_inicial, N//2) + fuente(f0,Ts,fase_inicial + np.pi, N//2)

def ejercicio_24():

    f0 = 1000
    fase_inicial = np.pi/2
    N = 3000
    f_muestreo = 100*f0
    Ts = 1/f_muestreo
    K= 1 #no hay un valor definido de él para este inciso.

    onda_error  = fuente(f0,Ts,fase_inicial, N//2) + fuente(f0,Ts,fase_inicial + np.pi, N//2)

    onda_salida = PLL(onda_error, 'rc', 2, 220, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)
    graficar_error(onda_entrada, onda_salida)

    return 0

def ejercicio_25():

    f0 = 1000
    fase_inicial = np.pi/2
    N = 3000
    f_muestreo = 100*f0
    Ts = 1/f_muestreo
    K = 1 #no hay un valor definido de él para este inciso.

    onda_salida = PLL(onda_error, 'lead-lag activo', np.sqrt(2)/2, 180, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)
    graficar_error(onda_entrada, onda_salida)

    return 0

# 6.2 Errores de frecuencia

onda_error = fuente(f0, Ts, fase_inicial, N//2) + fuente(f0*1.1, Ts, fase_inicial + np.pi, N//2)  

def ejercicio_26_a_28(wn):
  
    f0 = 1000
    fase_inicial = np.pi/2
    N = 3000
    f_muestreo = 100*f0
    Ts = 1/f_muestreo
    K= 1 #no hay un valor definido de él para este inciso.

    onda_salida = PLL(onda_error, 'rc', np.sqrt(2)/2, wn, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)#, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_error(onda_entrada, onda_salida)

    return 0

def ej_d():
    ejercicio_26_a_28(220)
    ejercicio_26_a_28(450)
    ejercicio_26_a_28(450) # Posible error en el enunciado

def ejercicio_29_a_31(wn):

    f0 = 1000
    fase_inicial = np.pi/2
    N = 3000
    f_muestreo = 100*f0
    Ts = 1/f_muestreo
    K= 1 #no hay un valor definido de él para este inciso.

    onda_salida = PLL(onda_error, 'lead-lag activo', np.sqrt(2)/2, wn, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)
    graficar_error(onda_entrada, onda_salida)

    return 0

def ej_c():
    ejercicio_29_a_31(180)
    ejercicio_29_a_31(120)
    ejercicio_29_a_31(80)


def ejercicio_32():

    onda_error = fuente(f0*1.03,Ts,fase_inicial, N//2) + fuente(f0*1.03, Ts, fase_inicial + np.pi, N//2)

    ejercicio_26_a_28(220)
    ejercicio_26_a_28(450)
    ejercicio_26_a_28(450)
    
    ejercicio_29_a_31(180)
    ejercicio_29_a_31(120)
    ejercicio_29_a_31(80)

    return 0

# 6.3 Rampa en frecuencia

# Ejercicio 33

def fuente_fvar(f_inicial, f_final, Ts, fase_inicial, N):
    
    salida = []
    m = (f_final-f_inicial)/(N-1)                                  # Se puede dividir por tiempo. En ese caso hay que corregir por que se multiplica abajo.

    for i in range(N):

        f = f_inicial+m*i
        salida.append([i*Ts,np.sin(2*np.pi*f*i*Ts + fase_inicial)])  # Añade un nuevo punto a la lista.

    return salida

def ejercicio_33():
  
    f0 = 1000
    Ts = 1/(100*f0)
    N  = 1000
  
    fase_inicial = np.pi/2
    onda_entrada = fuente_fvar(f0, 1.1*f0, Ts, fase_inicial, N)    #falta valores de N y Ts para que se ejecute.
    
    return onda_entrada

def ejercicio_34():

    onda_salida = PLL(onda_entrada, 'rc', np.sqrt(2)/2, 450, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)
    graficar_error(onda_entrada, onda_salida)

    return 0

def ejercicio_35():

    onda_salida = PLL(onda_entrada, 'lead-lag activo', np.sqrt(2)/2, 180, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)
    graficar_error(onda_entrada, onda_salida)
    
    return 0

def ejercicio_36():

    onda_salida = PLL(onda_entrada, 'lead-lag activo', np.sqrt(2)/2, 280, f0, K, Ts)
    graficar(onda_salida, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_lissajous(onda_entrada, onda_salida)#, 'Tiempo (s)', 'Amplitud (V)', 'Señal filtrada')
    graficar_error(onda_entrada, onda_salida)#, 'Tiempo (s)', 'Amplitud (V)', 'Error señal')

    return 0

# 6.4 Demodulación Coherente de una Señal

# Primer parte: estructura del transmisor

def gen_cod(Ts, Tb, N):

    salida = []
    step = int(Tb/Ts)

    for i in range(0,N,step):
      
        valor = np.round(np.random.rand())
        
        for j in range(i,i+step):
          
            salida.append([Ts*j,valor])

    return salida

def ejercicio_37():
  
    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo
    Tb = 2          # Período pulsos
    Ts = 1/fs       # Período muestreo
    N  = Nd*Tb*fs   # Cantidad de muestras

    salida_gen = gen_cod(Ts, Tb, N)
    graficar(salida_gen, 'Tiempo (s)', 'Amplitud (V)', 'Salida del Generador de Código', 'gen_cod')

    return 0

def respuesta_filtro(N,a,Tb,Fs):

    lista = rcosfilter(N, a, Tb, Fs)

    respuesta = []

    for i in range(N):
        respuesta.append([lista[0][i], lista[1][i]])
        
    return respuesta

# Ejercicio 38

def ejercicio_38():
    
    Fs = 1
    a = 0.5
    N = 100
    Tb = 20

    respuesta = respuesta_filtro(N, a, Tb, Fs)
          
    graficar(respuesta,'Tiempo (s)', 'Amplitud (V)', 'Filtrado')
    graficar(fourier(respuesta),'Tiempo (s)', 'Amplitud (V)', 'Filtrado')

# Ejercicio 39

def ejercicio_39_y_40(Tb):
    
    N = 1000
    Fs = 1
    a = 0.5
    Tb = 20
      
    lista = rcosfilter(N, a, Tb, Fs)
      
    transferencia = []
    for i in range(N):
        transferencia.append([lista[0][i], lista[1][i]])
      
    graficar(transferencia,'Tiempo (s)', 'Amplitud (V)', 'Transferencia')

def ej_b():
    ejercicio_39_y_40(2)
    ejercicio_39_y_40(1)

# Ejercicio 40

def ejercicio_40():

    Fs = 1
    a  = 0.5
    N  = 100
    Tb = 1

    respuesta = respuesta_filtro(N, a, Tb, Fs)
          
    graficar(respuesta,'Tiempo (s)', 'Amplitud (V)', 'Filtrado')

    lista = rcosfilter(N, a, Tb, Fs)
      
    transferencia = []
    for i in range(N):
        transferencia.append([lista[0][i], lista[1][i]])

    graficar(transferencia,'Tiempo (s)', 'Amplitud (V)', 'Transferencia')


# **Ejercicio 41**

def ejercicio_41():

    m = 1             # Índice de modulación
    f0 = 1000         # Frecuencia de la portadora

    salida_mod = []

    for i in range(len(respuesta)):
        salida_mod.append([respuesta[i][0], np.sin(2*np.pi*f0*respuesta[i][0])*m*respuesta[i][0]])
      
    graficar(salida_mod, 'Tiempo (s)', 'Amplitud (V)', 'Señal de salida modulada')


# Segunda parte: estructura del receptor

def emisor(Tb=2, a=0.5, f0=1000, m=1):

    Nd = 10         # Cantidad de pulsos
    fs = 200        # Frecuencia de muestreo

#    Tb = 2          # Período pulsos
#    f0 = 1000   # Frecuencia de la onda portadora
#    m = 1       # Índice de modulación

    Ts = 1/fs       # Período muestreo
    N = Nd*Tb*fs    # Cantidad de muestras

    Fs = 1  #

    onda_cod = gen_cod(Ts, Tb, N)               # Genera la onda con la información

    respuesta = respuesta_filtro(2*N,a,Ts,2*Fs) # Genera la respuesta del filtro a un pulso
    
    onda_salida = []                            # Genera la onda que saldrá del emisor
    
    for i in range(N):
        valor = 0
        for j in range(N):
            valor += onda_cod[j][1]*respuesta[4000+i-j][1]  # Genera el valor del filtro
        onda_salida.append([onda_cod[i][0],np.sin(2*np.pi*f0*onda_cod[i][0])*valor]) # Junta la señal inicial, el filtro y la portadora.

    return onda_salida

# La portadora del transmisor será de 1.05*f0.

def ejercicios_42_a_45(tipo, omega, K):

    xr = emisor(2, 0.5, 1050, 1)
    xi = np.sqrt(2)/2

    salida_pll = PLL(xr, tipo, xi, omega, f0, K, Ts)

    R1 = 1/(2*np.pi*(0.6)*f0)    # Valores algo arbitrarios.
    R2 = 0
    C  = 1

    salida_detector = filtro(salida_pll, estado_inicial, 'rc', C, R1, R2, Ts)

    Fs = 1
    a = 0.5
    fs = 200
    Tb = 1/fs
    N = 4000

    respuesta = 1*respuesta_filtro(8000,a,Tb,Fs)    # Genera la respuesta del filtro a un pulso
    #debe ser multiplicado por 0.01
    
    salida_filtro = []                            # Genera la onda que saldrá del emisor
    
    for i in range(N):
        valor = 0
        for j in range(N):
            valor += salida_detector[j][1]*respuesta[4000+i-j][1]  # Genera el valor del filtro
        salida_filtro.append([salida_detector[i][0],valor])        # Junta la señal inicial y el filtro
    
    graficar(salida_pll,'Tiempo (s)', 'Amplitud (V)', 'Salida del PLL')
    graficar(salida_detector,'Tiempo (s)', 'Amplitud (V)', 'Salida del detector rc')
    graficar(salida_filtro,'Tiempo (s)', 'Amplitud (V)', 'Salida del filtro FIR')
    graficar_lissajous(xr, salida_pll)
    graficar_lissajous(xr, salida_detector)
    graficar_lissajous(xr, salida_filtro)

def ej_a():
    ejercicios_42_a_45('rc', 120, 100)
    ejercicios_42_a_45('rc', 220, 100)
    ejercicios_42_a_45('rc', 450, 100)
    ejercicios_42_a_45('lead-lag activo', 450, 100)