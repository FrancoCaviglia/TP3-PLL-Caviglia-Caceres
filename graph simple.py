# -*- coding: utf-8 -*-
import matplotlib, sys
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk

master = tk.Tk()
#-------------------------------------------------------------------------------

f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)
t = arange(0.0,3.0,0.01)
s = sin(2*pi*t)
a.plot(t,s)

dataPlot = FigureCanvasTkAgg(f, master=master)
dataPlot.show()
dataPlot.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#-------------------------------------------------------------------------------
master.mainloop()