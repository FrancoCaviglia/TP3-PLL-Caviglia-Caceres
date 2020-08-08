# -*- coding: utf-8 -*-
                                          
"""

Revisado por última vez el Viernes 7 de Agosto a las 22:00 2020.
@author: Franco Caviglia, Joan Joel Cáceres

"""

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from numpy import abs
from scipy import fftpack
from functools  import partial
from enun_resp  import enunciados, respuestas
from caratula   import caratula_1, caratula_2, caratula_3, plt
from soluciones import *

""" En este archivo se arma la interfaz gráfica. Para mostrar los resultados necesita las funciones que se encuentran en
    soluciones.py. Cada parte de la interfaz se corresponde con un "widget", que en este caso pueden ser Frame, Button,
    Label, Entry. Los atributos de cada uno de estos widget dan su geometría, aspecto y funcionalidad. Cada uno de los
    widget creados es empaquetado utilizando las funciones .pack(), .grid(), o .place(). La primera depende de que se haya
    empaquetado antes, mientras que la segunda ubica al widge en una grilla para la cual hay que especificar la fila y
    columna. En cada frame sólo se puede utilizar un tipo de función para el empaquetado. El árbol de inclusión es
   
    ventana _____ frame_1 _____ autores (pack)                                                                                (pack)
              |             |__ título  (pack)
              |             |__ materia (pack)
              |
              |__ frame_2 _____ frame_2_1 ___ frame ___ boton ___ ejercicio_i (grid)                              (pack)      (pack)
                            |
                            |__ frame_2_2 _____ frame_2_2_1 _____ frame_2_2_1_1 ___ parámetros  (grid)            (pack)
                                            |                 |__ frame_2_2_1_2 ___ figura      (pack)
                                            |
                                            |__ frame_2_2_2 _____ canvas_widget_1 (grid)                          (pack)
                                            |                 |__ canvas_widget_2 (grid)
                                            |                 |__ canvas_widget_2 (grid)
                                            |
                                            |__ frame_2_2_3 _____ frame ___ botones_grafica(frame, 0)  (grid)     (pack)
                                            |                 |__ frame ___ botones_grafica(frame, 1)  (grid)
                                            |                 |__ frame ___ botones_grafica(frame, 2)  (grid)
                                            |
                                            |__ frame_2_2_4 _____ ejercicio_enunciado (grid)                      (pack)
                                                              |__ ejercicio_respuesta (grid)
"""

estado_figuras = [['A',0],['B',1],['C',2]] # Guarda cual de los set de datos A, B, C, D, E, F están en cada una da las tres gráficas.

ventana = tk.Tk()
ventana.title('Simulador PLL')

screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
ventana.geometry(f'{screen_width}x{screen_height-80}')

def crear_figura(cord_x, cord_y, leyenda_x, leyenda_y, encabezado, logx):

    #plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    
    plt.rc('font', size=9)       
    plt.rc('axes', titlesize=9)
    plt.rc('axes', labelsize=9)
    plt.rc('xtick', labelsize=9)
    plt.rc('ytick', labelsize=9)
    plt.rc('legend', fontsize=9)
    plt.rc('figure', titlesize=9)
    
    fig = plt.figure(figsize=(4.4, 3.2))

    if logx:
        plt.xscale('log')
        
    plt.plot(cord_x, cord_y, 'b')#, label=referencia)
    #plt.title(r'\textrm{'+encabezado+'}', fontsize=9)
    #plt.xlabel(r'\textrm{'+leyenda_x+'}', fontsize=9)
    #plt.ylabel(r'\textrm{'+leyenda_y+'}', fontsize=9)
    plt.margins(0.01)
    plt.grid()
    plt.tight_layout()
 
    return fig

def actualizar_figura(cord_x, cord_y, leyenda_x, leyenda_y, encabezado, j, i, logx = False):
    
    global canvas_lista, plots, canvas_widget, estado_figuras
    
    plt.close(plots[i])                                         # Destruye el plot de la gráfica. Sirve para desocupar memoria.
    
    canvas_widget[i].destroy()                                  # Destruye el widget asociado a la figura anterior
      
    plots[i] = crear_figura(cord_x, cord_y, leyenda_x, leyenda_y, encabezado, logx)  # Fabrica la figura correspondiente
    
    canvas_lista[i] = FigureCanvasTkAgg(plots[i], master=frame_2_2_2)            # Fabrica el objeto para mostrar la figura, y lo asocia a la ventana correcta.
    canvas_widget[i] = canvas_lista[i].get_tk_widget()
    canvas_widget[i].grid(row=0, column=i, padx = 1, pady = 1, sticky='NSWE')    # Empaqueta la figura
    
    estado_figuras[i] = [encabezado[-1], j]
    
def actualizar_dominio(dominio, i):
    
    global datos, leyendas
    
    estado = estado_figuras[i] # Primero separa el estado de la gráfica que se desea moficiar. 
                               # estado = [ 'LETRA', Numero de dato]
    
    if dominio == 'Tiempo (s)':
        actualizar_figura(datos[estado[1]][0], datos[estado[1]][1], dominio, leyendas[1], 'Grafica '+estado[0], estado[1], i)
        
    elif dominio == 'Frecuencia (Hz)' and datos[estado[1]] != [[],[]]:
        
        Ts = datos[estado[1]][0][1] - datos[estado[1]][0][0]    # Calcula cual es período muestral de los datos
        x_fourier = fftpack.fftshift(fftpack.fftfreq(len(datos[estado[1]][0]), Ts)) # Arma el dominio de la transforamda de Fourier
        y_fourier = abs(fftpack.fftshift(fftpack.fft(datos[estado[1]][1])))              # Fabrica y ordena la transformada de Fourier.
    
        actualizar_figura(x_fourier, y_fourier, dominio, leyendas[1], 'Grafica '+estado[0], estado[1], i, logx = True)
    
    else: 
        pass
    
def cerrar():           # No modificar este nombre
    ventana.quit()     # Detiene mainloop
    ventana.destroy()  # Es necesario en Windows para prevenir el error fatal de python: PyEval_RestoreThread: NULL tstate

frame_1 = tk.Frame(master=ventana, relief = tk.RAISED, borderwidth=2, bg="white")
frame_2 = tk.Frame(master=ventana, relief = tk.RAISED, borderwidth=2, bg="white")

frame_1.pack(fill=tk.BOTH, side=tk.TOP,    expand=True)
frame_2.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
autores = tk.Label(master=frame_1, text="Franco Caviglia, Joan Cáceres", fg="white", bg="black", width=10, height=1)
titulo  = tk.Label(master=frame_1, text="Simulador PLL",                 fg="white", bg="black", width=70, height=1, font=24)
materia = tk.Label(master=frame_1, text="Física Experimental II",        fg="white", bg="black", width=10, height=1)

autores.pack(fill=tk.BOTH, side=tk.LEFT, anchor=tk.NW,     expand=True)
titulo.pack(fill=tk.BOTH,  side=tk.LEFT, anchor=tk.CENTER, expand=True)
materia.pack(fill=tk.BOTH, side=tk.LEFT, anchor=tk.NE,     expand=True)

frame_2_1 = tk.Frame(master=frame_2, relief = tk.RAISED, borderwidth=2, bg="#979797")
frame_2_2 = tk.Frame(master=frame_2, relief = tk.RAISED, borderwidth=2, bg="#A7A7A7")

frame_2_1.pack(fill=tk.Y,    side=tk.LEFT)
frame_2_2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

frame_2_2_1 = tk.Frame(master=frame_2_2, bg="#A7A7A7")
frame_2_2_2 = tk.Frame(master=frame_2_2, bg="#A7A7A7")
frame_2_2_3 = tk.Frame(master=frame_2_2, bg="#A7A7A7")
frame_2_2_4 = tk.Frame(master=frame_2_2, bg="#A7A7A7")

frame_2_2_1.pack(fill=tk.BOTH, expand=True)
frame_2_2_2.pack(fill=tk.BOTH, expand=True)
frame_2_2_3.pack(fill=tk.BOTH, expand=True)
frame_2_2_4.pack(fill=tk.BOTH, expand=True)

frame_2_2_1_1 = tk.Frame(master=frame_2_2_1, relief = tk.GROOVE, bg="black")
frame_2_2_1_2 = tk.Frame(master=frame_2_2_1, relief = tk.GROOVE, bg="#9D9D9D")

frame_2_2_1_1.pack(fill=tk.BOTH, side=tk.LEFT,  expand=True)
frame_2_2_1_2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

lb_muestras  = tk.Label(master=frame_2_2_1_1, text="Número de muestras (N): ", fg="white", bg="black")
ent_muestras = tk.Entry(master=frame_2_2_1_1, width=9)
lb_muestras.grid(row=0, column=0,  sticky="w")
ent_muestras.grid(row=0, column=1, sticky="e")

lb_freq      = tk.Label(master=frame_2_2_1_1, text="Frecuencia entrada (Hz): ", fg="white", bg="black")
ent_freq     = tk.Entry(master=frame_2_2_1_1, width=9)
lb_freq.grid(row=0,  column=2, sticky="w")
ent_freq.grid(row=0, column=3, sticky="e")    

lb_freq_m    = tk.Label(master=frame_2_2_1_1, text="Frecuencia de muestreo (N/s): ", fg="white", bg="black")
ent_freq_m   = tk.Entry(master=frame_2_2_1_1, width=9)
lb_freq_m.grid(row=1, column=0,  sticky="w")
ent_freq_m.grid(row=1, column=1, sticky="e") 

lb_fase      = tk.Label(master=frame_2_2_1_1, text="Fase inicial de entrada: ", fg="white", bg="black")
ent_fase     = tk.Entry(master=frame_2_2_1_1, width=9)
lb_fase.grid(row=1, column=2,  sticky="w")
ent_fase.grid(row=1, column=3, sticky="e") 

lb_amort     = tk.Label(master=frame_2_2_1_1, text="Factor de amortiguamiento: ", fg="white", bg="black")
ent_amort    = tk.Entry(master=frame_2_2_1_1, width=9)
lb_amort.grid(row=2, column=0,  sticky="w")
ent_amort.grid(row=2, column=1, sticky="e") 

lb_freq_p    = tk.Label(master=frame_2_2_1_1, text="Frecuencia propia (Hz): ", fg="white", bg="black")
ent_freq_p   = tk.Entry(master=frame_2_2_1_1, width=9)
lb_freq_p.grid(row=2, column=2,  sticky="w")
ent_freq_p.grid(row=2, column=3, sticky="e") 

lb_freq_v     = tk.Label(master=frame_2_2_1_1, text="Frecuencia natural VCO (Hz): ", fg="white", bg="black")
ent_freq_v   = tk.Entry(master=frame_2_2_1_1, width=9)
lb_freq_v.grid(row=3, column=0,  sticky="w")
ent_freq_v.grid(row=3, column=1, sticky="e") 

lb_ganan    = tk.Label(master=frame_2_2_1_1, text="Ganancia de lazo VCO: ", fg="white", bg="black")
ent_ganan   = tk.Entry(master=frame_2_2_1_1, width=9)
lb_ganan.grid(row=3, column=2,  sticky="w")
ent_ganan.grid(row=3, column=3, sticky="e")

lb_simb     = tk.Label(master=frame_2_2_1_1, text="Período de símbolos: ", fg="white", bg="black")
ent_simb    = tk.Entry(master=frame_2_2_1_1, width=9)
lb_simb.grid(row=4, column=0,  sticky="w")
ent_simb.grid(row=4, column=1, sticky="e") 

lb_filtro    = tk.Label(master=frame_2_2_1_1, text="Tipo de filtro: ", fg="white", bg="black")
ent_filtro   = tk.Entry(master=frame_2_2_1_1, width=9)
lb_filtro.grid(row=4, column=2,  sticky="w")
ent_filtro.grid(row=4, column=3, sticky="e") 

lb_frr    = tk.Label(master=frame_2_2_1_1, text="Factor de roll-off: ", fg="white", bg="black")
ent_frr   = tk.Entry(master=frame_2_2_1_1, width=9)
lb_frr.grid(row=5, column=0,  sticky="w")
ent_frr.grid(row=5, column=1, sticky="e") 

lb_pulsos  = tk.Label(master=frame_2_2_1_1, text="Cantidad de pulsos: ", fg="white", bg="black")
ent_pulsos = tk.Entry(master=frame_2_2_1_1, width=9)
lb_pulsos.grid(row=6, column=0,  sticky="w")
ent_pulsos.grid(row=6, column=1, sticky="e") 

entradas = [ent_muestras, ent_freq_m,   ent_freq,   ent_fase, ent_amort, ent_freq_p,
                ent_simb,  ent_ganan, ent_freq_v, ent_filtro,   ent_frr, ent_pulsos]

salir = tk.Button(master=frame_2_2_1_1, text="Salir", command=cerrar)
salir.grid(row=6,column=3)

""" Arma el esquema del PLL dentro de frame_2_2_1_2 """ 

canvas_figura = tk.Canvas(master=frame_2_2_1_2, width = 685, height = 165)
img = tk.PhotoImage(master = frame_2_2_1_2, file="./imagen_1.pgm")
imgArea = canvas_figura.create_image(348, 85, anchor = tk.CENTER, image = img)
canvas_figura.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

""" frame_2_2_2 : tres graficas """

frame_2_2_2.grid_rowconfigure(0, weight=1, uniform="graficas")
frame_2_2_2.grid_columnconfigure([0,1,2], weight=1, uniform="graficas") 

plot_1 = caratula_1()                                      # Fabrica la figura correspondiente    
canvas_1 = FigureCanvasTkAgg(plot_1, master=frame_2_2_2)      # Fabrica el objeto para mostrar la figura, y lo asocia a la ventana correcta.
canvas_widget_1 = canvas_1.get_tk_widget()
canvas_widget_1.grid(row=0, column=0, padx = 1, pady = 1, columnspan=1, rowspan=1)  # Empaqueta la figura

plot_2 = caratula_2()                                      # Fabrica la figura correspondiente
canvas_2 = FigureCanvasTkAgg(plot_2, master=frame_2_2_2)      # Fabrica el objeto para mostrar la figura, y lo asocia a la ventana correcta.
canvas_widget_2 = canvas_2.get_tk_widget()
canvas_widget_2.grid(row=0, column=1, padx = 1, pady = 1, columnspan=1, rowspan=1)  # Empaqueta la figura

plot_3 = caratula_3()                                      # Fabrica la figura correspondiente
canvas_3 = FigureCanvasTkAgg(plot_3, master=frame_2_2_2)      # Fabrica el objeto para mostrar la figura, y lo asocia a la ventana correcta.
canvas_widget_3 = canvas_3.get_tk_widget()
canvas_widget_3.grid(row=0, column=2, padx = 1, pady = 1, columnspan=1, rowspan=1)  # Empaqueta la figura

canvas_lista = [canvas_1, canvas_2, canvas_3]
plots = [plot_1, plot_2, plot_3]                                    # Hay tres plots, uno por cada gráfica
canvas_widget = [canvas_widget_1, canvas_widget_2, canvas_widget_3] # Hay tres widgets, uno por cada gráfica   
    
""" frame_2_2_3 : botones de las graficas """

def botones_grafica(frame, j):
    
    global datos, leyendas
                
    button_1 = tk.Button(master=frame, text='A', width=3, height=1, bg="#C6C6C6", fg="black",
                         command = lambda : actualizar_figura(datos[0][0], datos[0][1], leyendas[0], leyendas[1], 'Grafica A', 0, j))
    button_1.grid(row=0, column=0, sticky = 'nsew')
    
    button_2 = tk.Button(master=frame, text='B', width=3, height=1, bg="#C6C6C6", fg="black",
                         command = lambda : actualizar_figura(datos[1][0], datos[1][1], leyendas[0], leyendas[1], 'Grafica B', 1, j))
    button_2.grid(row=0, column=1, sticky = 'nsew')

    button_3 = tk.Button(master=frame, text='C', width=3, height=1, bg="#C6C6C6", fg="black",
                         command = lambda : actualizar_figura(datos[2][0], datos[2][1], leyendas[0], leyendas[1], 'Grafica C', 2, j))
    button_3.grid(row=0, column=2, sticky = 'nsew')

    button_4 = tk.Button(master=frame, text='D', width=3, height=1, bg="#C6C6C6", fg="black",
                         command = lambda : actualizar_figura(datos[3][0], datos[3][1], leyendas[0], leyendas[1], 'Grafica D', 3, j))
    button_4.grid(row=0, column=3, sticky = 'nsew')

    button_5 = tk.Button(master=frame, text='E', width=3, height=1, bg="#C6C6C6", fg="black",
                         command = lambda : actualizar_figura(datos[4][0], datos[4][1], leyendas[0], leyendas[1], 'Grafica E', 4, j))
    button_5.grid(row=0, column=4, sticky = 'nsew')

    button_6 = tk.Button(master=frame, text='F', width=3, height=1, bg="#C6C6C6", fg="black",
                         command = lambda : actualizar_figura(datos[5][0], datos[5][1], leyendas[0], leyendas[1], 'Grafica F', 5, j))
    button_6.grid(row=0, column=5, sticky = 'nsew')
    
    intermedio = tk.Frame(master=frame, width=9, height=1, bg = "#A7A7A7")
    intermedio.grid(row=0, column=6, sticky = 'nsew')
    
    button_7 = tk.Button(master=frame, text='Tiempo', width=9, height=1, bg="#C6C6C6", fg="black",
                         command = lambda : actualizar_dominio('Tiempo (s)', j) )
    button_7.grid(row=0, column=7, sticky = 'nsew')

    button_8 = tk.Button(master=frame, text='Frecuencia', width=9, height=1, bg="#C6C6C6", fg="black",
                         command = lambda : actualizar_dominio('Frecuencia (Hz)', j) )
    button_8.grid(row=0, column=8, sticky = 'nsew')
                
for j in range(3):
    
    frame_2_2_3.columnconfigure(j, weight=1, minsize=40)
    frame_2_2_3.rowconfigure(j, weight=1, minsize=1)

    frame = tk.Frame(master=frame_2_2_3, relief=tk.RAISED, borderwidth=1)
    frame.grid(row=0, column=j, padx = 2, pady = 2)
    botones_grafica(frame, j)
        
""" frame_2_2_4 """
        
frame_2_2_4.columnconfigure(0, weight=1, minsize=90)
frame_2_2_4.rowconfigure([0,1], weight=1, minsize=4)
    
ejercicio_enunciado = tk.Label(master=frame_2_2_4, text="En esta sección aparecerá el enunciado del ejercicio seleccionado.",
                               width=160, height=3, wraplength=1090, bg="white", fg="black", relief = tk.RAISED, justify=tk.LEFT)
ejercicio_respuesta = tk.Label(master=frame_2_2_4, text="En esta sección aparecerá la respuesta del ejercicio seleccionado.",
                               width=160, height=5, wraplength=1090, bg="white", fg="black", relief = tk.RAISED, justify=tk.LEFT)

ejercicio_enunciado.grid(row=0, column=0, sticky = 'nsew')
ejercicio_respuesta.grid(row=1, column=0, sticky = 'nsew')

""" Fin frame_2_2_4 """

""" Comienzo frame_2_1 """

""" A partir de acá se generan las acciones a ejecutar por cada botón Ejercicio X. """

ejercicios = [ ejercicio_1,  ejercicio_2,  ejercicio_3,  ejercicio_4,  ejercicio_5,  ejercicio_6,  ejercicio_7,  ejercicio_8,  ejercicio_9,
              ejercicio_10, ejercicio_11, ejercicio_12, ejercicio_13, ejercicio_14, ejercicio_15, ejercicio_16, ejercicio_17, ejercicio_18, 
              ejercicio_19, ejercicio_20, ejercicio_21, ejercicio_22, ejercicio_23, ejercicio_24, ejercicio_25, ejercicio_26, ejercicio_27,
              ejercicio_28, ejercicio_29, ejercicio_30, ejercicio_31, ejercicio_32, ejercicio_33, ejercicio_34, ejercicio_35, ejercicio_36,
              ejercicio_37, ejercicio_38, ejercicio_39, ejercicio_40, ejercicio_41, ejercicio_42, ejercicio_43, ejercicio_44, ejercicio_45]

def ejercicio_boton(i):

    """ Construye la acción a seguir cada vez que se presiona en un botón Ejercicio i. Para los gráficos y parámetros
    utiliza las funciones definidas en soluciones.py """
    
    global img, canvas_figura, datos, leyendas, estado_figuras, ejercicio_enunciado, ejercicio_respuesta
    
    for j in range(3):
        actualizar_figura([], [], leyendas[0], leyendas[1], 'Grafica '+estado_figuras[j][0], estado_figuras[j][1], j)
    
    datos, leyendas, param = ejercicios[i]()
    
    # Actualiza la imagen del esquema según el ejercicio.
    
    if i<36:
        img = tk.PhotoImage(master = frame_2_2_1_2, file="./imagen_1.pgm")
        canvas_figura.itemconfig(imgArea, image = img) 
    else:
        img = tk.PhotoImage(master = frame_2_2_1_2, file="./imagen_2.pgm")
        canvas_figura.itemconfig(imgArea, image = img)

    # Actualiza el texto del enunciado y respuesta según el ejercicio.

    ejercicio_enunciado["text"] = f"Ejercicio {i+1}. "+enunciados[i]
    ejercicio_respuesta["text"] = respuestas[i]
    
    # Actualiza el texto de cada parámetro según lo devuelto por ejercicio_i().
    
    for i in range(len(entradas)):
        entradas[i].delete(0, tk.END)
        entradas[i].insert(0, f'{param[i]}')
    
ejercicios_arg = []
for i in range(45):    # Agarra cada función con ejercicios y crea nuevas funciones con los argumentos
    ejercicios_arg.append(partial(ejercicio_boton, i))

# Cada ejercicio corregirá dentro del espacio de nombres global el enunciado, la respuesta, y los 4 posibles datos a representar
# Las 45 funciones a utilizar se encuentran entonces dentro de la lista ejercicios_arg
    
""" Comienzo frame_2_1 """ 

for i in range(3):
    frame_2_1.columnconfigure(i, weight=1)
    for j in range(15):
        frame_2_1.rowconfigure(j, weight=1)
    
        frame = tk.Frame(master=frame_2_1, relief=tk.RAISED, borderwidth=1)
        
        frame.grid(row=j, column=i, padx = 2, pady = 3, sticky = 'nsew')
        
        numero = i*15+j+1

        boton = tk.Button(master=frame, text=f"Ejercicio {numero}", width=9, height=1, bg="#C6C6C6", fg="black", command = ejercicios_arg[numero-1] )
        boton.pack(fill=tk.BOTH, expand=True)

""" Fin frame_2_1 """

ventana.mainloop()  # Genera el ciclo que da lugar a la interfaz interactiva.
