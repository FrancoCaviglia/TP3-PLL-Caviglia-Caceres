# -*- coding: utf-8 -*-

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from functools import partial

tn = []
for i in range(500):
    tn.append(i/500)

xn = []
for i in range(len(tn)):
    xn.append(0.5)

yn = []
for i in range(len(tn)):
    yn.append(np.cos(2*np.pi*tn[i]))
    
zn = []
for i in range(len(tn)):
   zn.append(np.sin(2*np.pi*tn[i]))
                
tod = [yn, zn]

root = tk.Tk()

def crear_figura(tn, xn):
         
    f = plt.figure()
    plt.plot(tn, xn)
    
    return f

def actualizar_figura(xn):
    
    global canvas_widget, f
    
    plt.close(f)
    
    canvas_widget.destroy()
    
    f = crear_figura(tn, xn)
        
    canvas = FigureCanvasTkAgg(f, master=frame_1)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    #canvas.show()

frame_1 = tk.Frame(master=root, width=500, height=400)
frame_1.pack(fill=tk.BOTH, expand=1)

frame_2 = tk.Frame(master=root)
frame_2.pack(fill=tk.BOTH, expand=1)

f = crear_figura(tn, xn)

canvas = FigureCanvasTkAgg(f, master=frame_1)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#canvas.show()

cambio = []
for i in range(2):
    cambio.append(partial(actualizar_figura, tod[i]))
    
button_1 = tk.Button(text="Seno",   width=5, height=1, bg="#C6C6C6", fg="black", master=frame_2, command = cambio[0])
button_1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

button_2 = tk.Button(text="Coseno", width=5, height=1, bg="#C6C6C6", fg="black", master=frame_2, command = cambio[1])
button_2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

root.mainloop()

#toolbar = NavigationToolbar2TkAgg(canvas, frame )
#toolbar.pack()
#toolbar.update()

#root.update()
#root.deiconify()