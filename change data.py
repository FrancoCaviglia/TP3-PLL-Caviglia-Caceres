# -*- coding: utf-8 -*-

import tkinter

variable = "data"

def changeVariable():
    global variable
    variable = "different data"

def printVariable():
    global variable
    print(variable)

window = tkinter.Tk()
button1 = tkinter.Button(window, command=changeVariable)
button1.pack()
button2 = tkinter.Button(window, command=printVariable)
button2.pack()

window.mainloop()