# Trabajo práctico virtual N°3
## Física Experimental II - Instituto Balseiro
### Franco Caviglia, Joan Joel Cáceres

Dentro de la carpeta PLL se encuentran los archivos necesarios para la ejecución del simulador. Dentro de esta se encuentran:

* **GUI.py** Contiene todo lo necesario para el armado de la interfaz gráfica en base a la biblioteca *Tkinter*. Es el archivo principal, importa y utiliza a todos los siguientes.
* **auxiliares.py** Contiene todas las funciones necesarias para las simulaciones, tales como *fuente(f0, Ts, fase_inicial, N)*, *detector(xr, xv)*, *filtro(xd, zi, tipo, C, R1, R2, Ts)*, entre otras.
* **soluciones.py** Contiene las funciones de la forma *ejercicio_X()*, las cuales devuelven la información necesaria para mostrar en la GUI.
* **enunciados.py** Contiene dos listas de nombre *enunciados*, *respuestas* las cuales contienen el texto a mostrar en las secciones *ejercicios_enunciados*, *ejercicios_respuestas* dentro de la interfaz gráfica (GUI) respectivamente.
* **caratula.py** Contiene la información para el armado de las figuras a la hora de arrancar la interfaz gráfica.
* **imagen_1.pgm** Contiene el esquema del circuito PLL en un formato soportado por la biblioteca *Tkinter*.
* **imagen_2.pgm** Contiene el esquema del par emisor-receptor en un formato soportado por la biblioteca *Tkinter*.

Fuera de la carpeta PLL se encuentran archivos "borrador" con algunos ejemplos de juguete.

