from tkinter import *
from time import sleep

root = Tk()
var = StringVar()
var.set('hello')

l = Label(root, textvariable = var)
l.pack()

for i in range(6):
    sleep(2) # Need this to slow the changes down
    var.set('goodbye' if i%2 else 'hello')
    root.update_idletasks()

root.quit()     # Detiene mainloop
root.destroy()  # Es necesario en Windows para prevenir el error fatal de python: PyEval_RestoreThread: NULL tstate