# -*- coding: utf-8 -*-

import tkinter as tk

window_1 = tk.Tk()
window_2 = tk.Tk()

frame_1 = tk.Frame(master=window_1, relief = tk.FLAT, 
                   borderwidth=2)

frame_2 = tk.Frame(master=window_2)

label_1 = tk.Label(master=frame_1, text='A')
label_1.pack()

label_2 = tk.Label(master=frame_2, text='B')
label_2.pack()

frame_1.pack(fill = tk.X)
frame_2.pack()

window_1.mainloop()
window_2.mainloop()

# Geometry managers:
# .pack()
# .place()
# .grid()
# Cada Frame puede usar sólo un tipo
