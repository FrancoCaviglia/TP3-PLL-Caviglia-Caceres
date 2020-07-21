# -*- coding: utf-8 -*-

import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

from pandas import DataFrame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar(v, leyenda_x='x', leyenda_y='y', encabezado='Grafica', nombre_archivo='untitle', referencia='Tension'):
    
    x = []
    y = []
    
    for i in range(len(v)):
        x.append(v[i][0])
        y.append(v[i][1])
         
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
     
    f = plt.figure()
    
    plt.plot(x, y, label=referencia)
    # set labels (LaTeX can be used)
    plt.title(r'\textbf{'+leyenda_y+'}', fontsize=11)
    plt.xlabel(r'\textbf{'+leyenda_x+'}', fontsize=11)
    plt.ylabel(r'\textbf{'+encabezado+'}', fontsize=11)
#   plt.margins(0,0.05)
    plt.grid()
    plt.legend()
    plt.show()
    
    f.savefig(nombre_archivo+".pdf", bbox_inches='tight')

root = tk.Tk() 

figure1 = plt.Figure(figsize=(6,5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')

figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
ax2.set_title('Year Vs. Unemployment Rate')

figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price']) 
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')

root.mainloop()