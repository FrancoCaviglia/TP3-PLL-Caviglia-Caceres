# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:53:45 2020

@author: Libre
"""

import tkinter as tk

# Create a window object
window = tk.Tk()

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)


# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# Run the event loop
window.mainloop()
