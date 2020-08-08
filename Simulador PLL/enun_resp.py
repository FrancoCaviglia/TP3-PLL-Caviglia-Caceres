# -*- coding: utf-8 -*-

"""

Revisado por última vez el Viernes 7 de Agosto a las 22:00 2020.
@author: Franco Caviglia, Joan Joel Cáceres

"""

enunciados = [
              "Construir una función en Python que genere N muestras de la señal de entrada al PLL: fuente(f0, Ts, fase inicial, N). Donde f0 es la frecuencia de la señal, Ts es el periodo entre muestras (periodo de muestreo), fase inicial es la fase inicial de la señal, y N es el número total de muestras de la señal a generar.",
              "Utilizando la función construida representar la señal de entrada al PLL para N = 1000 muestras, f0 = 1 kHz, fase inicial = π/2, y periodo de muestreo: Ts = 1/(100f0). Con la función construida podemos fácilmente generar una señal de entrada al PLL con un salto de fase en un instante temporal determinado.",
              "Utilizando la función construida representar la señal de entrada al PLL en las mismas condiciones anteriores, pero introduciendo un salto de fase de valor π en la muestra: N/2.",
              "Construir una función en Python que implemente el detector de fases entre una muestra temporal de la señal de entrada xr y una muestra temporal de la señal del VCO (x_v = x_VCO):\ndetector(xr, xv).",
              "Usando las funciones anteriores construya dos señales de frecuencia f0 = 1 kHz, una con fase inicial cero y la otra con fase inicial π/4. Pasar las dos señales por el detector de fases. Tenga en cuenta que debe pasar el detector muestra a muestra con un bucle temporal. Representar la señal resultante en tiempo y frecuencia. Comentar el resultado obtenido. Interpretar el significado de la componente continua obtenida.",
              "Repetir el ejercicio con dos señales, una con fase inicial cero y la otra con fase inicial π/2. ¿Qué fase detecta el detector de fase en este caso? Comentar los resultados obtenidos.",
              "Utilizando todas las consideraciones anteriores, construir una función en Python que sirva para realizar el filtrado muestra a muestra de la señal de entrada (xd): filtro(xd, estado inicial, tipo, C, R1, R2, Ts). La variable (tipo) podría tomar los valores “rc” y “lead-lag activo”, para implementar en cada caso la correspondiente función de transferencia. Para el filtro “rc” y el “lead-lag activo” tomar como parámetros de entrada el coeficiente de amortiguamiento (ξ), y la pulsación propia (wn). Calcular los restantes componentes del filtro a partir de estos dos parámetros de entrada, suponiendo R = R1 = R2 = C.",
              "Introducir una función δ como señal de entrada al filtro “rc”, con el fin de obtener la respuesta al impulso y la función de transferencia del filtro. Dibujar la respuesta al impulso y la función de transferencia obtenida para los tres casos siguientes: (wn = 2, ξ = √ 2/2), (wn = 100, ξ = √2/2) y (wn = 2, ξ = 5). Comentar cómo varía en cada caso la respuesta del filtro.",
              "Tomando N = 2000 muestras, aplicar el filtro “rc” en los tres casos anteriores: (wn = 2, ξ = √ 2/2), (wn = 100, ξ = √2/2) y (wn = 2, ξ = 5). Representar la señal después del filtro tanto en tiempo como en frecuencia. Para la representación de señales en frecuencia en Python ver el comando fft.",
              "Repetir el ejercicio 9 pero aplicando el filtro “lead-lag activo”, con los valores: (wn = 2, ξ = √2/2), (wn = 100, ξ = √2/2) y (wn = 2, ξ = 0,1). Comentar los resultados obtenidos para este filtro.",
              "En base al desarrollo anterior, construir una función que, dada la frecuencia actual (f = f0 +Kxc(t)) y la fase en el instante t, calcule la fase en el instante siguiente (t+Ts): fase final = fase(Ts,f,fase inicial). Al construir la función, asegurarse que la fase de salida estará comprendida entre el intervalo (0, 2π).",
              "Generar en primer lugar la señal moduladora (o señal de control, xc(t)) usando la función “fuente” ya construida (tomar como fase inicial cero). Representar la señal en tiempo y frecuencia.",
              "Obtener la señal a la salida del VCO sin introducir señal de control (K = 0). Representar la señal en tiempo y frecuencia. Comentar el resultado obtenido.",
              "Obtener la señal a la salida del VCO introduciendo la señal de control con una ganancia K = 100. Dibujar la señal obtenida en tiempo y frecuencia. ¿Ha obtenido la señal modulada en frecuencia?",
              "Utilizando el filtro “rc”, ajustar los parámetros del bucle a (ξ = √2/2, wn = 180). Representar la señal a la salida del filtro con el fin de comprobar el tipo de amortiguamiento del bucle. Repetir con un factor de amortiguamiento de (ξ = 0,3) y (ξ = 2,0) para comprobar cómo cambia el amortiguamiento del bucle con el parámetro de amortiguamiento ξ. Representar todas las gráficas.",
              "Para los tres casos anteriores representar el diagrama de Lissajous y la gráfica de error entre la señal de salida del VCO y la señal de entrada. ¿Consigue engancharse el PLL en fase?",
              "Para comprobar como afecta el ancho de banda del filtro, repetir el ejercicio con ξ = √2/2, wn = 120). ¿Qué ocurre al disminuir el ancho de banda del filtro?",
              "Utilizando el filtro “lead-lag activo”, comprobar el enganche del PLL para unos parámetros de bucle: (ξ = √2/2, wn = 40).",
              "Comprobar el enganche del filtro si se aumenta el ancho de banda a: (ξ = √2/2, wn = 120). ¿Se comporta el PLL igual que antes con el ancho de banda del filtro?",
              "Con el filtro “rc”, ajustar los parámetros del bucle a: (ξ = 2,0, wn = 220). ¿Consigue engancharse el PLL al introducir el error de fase?",
              "Repetir el proceso para unos parámetros: (ξ = √2/2, wn = 220). Comentar las diferencias que observa.",
              "Con el filtro “lead-lag activo”, ajustar los parámetros del bucle a: (ξ = √2/2, wn = 80). ¿Se engancha correctamente el PLL?",
              "Repetir el proceso para unos parámetros: (ξ = √2/2, wn = 180). ¿Qué ocurre con la velocidad de enganche del PLL?",
              "Con el filtro “rc”, ajustar los parámetros del bucle a: (ξ = 2,0, wn = 220 ). ¿Consigue engancharse el PLL al introducir el error de fase? ¿Porqué?",
              "Con el filtro “lead-lag activo”, ajustar los parámetros del bucle a: (ξ = √2/2, wn = 180). ¿Se engancha correctamente el PLL? ¿Porqué cree que ocurre esto?",
              "Con el filtro “rc”, ajustar los parámetros del bucle a: (ξ = √2/2, wn = 220). ¿Consigue engancharse el PLL al introducir el error de frecuencia?",
              "Repetir el experimento tomando los siguientes parámetros de bucle: (ξ = √2/2, wn = 450). Interprete el resultado obtenido.",
              "Repetir el experimento tomando los siguientes parámetros de bucle: (ξ = √2/2, wn = 450). Interprete el resultado obtenido. En concreto, ¿qué sucede con el error de fase del PLL? ¿Porqué?",
              "Con el filtro “lead-lag activo”, ajustar los parámetros del bucle a: (ξ = √2/2, wn = 180). ¿Se engancha correctamente el PLL?",
              "Repetir el ejercicio, si reduce la pulsación propia a wn = 120, ¿se engancha el PLL correctamente? ¿Por qué?",
              "Repetir el ejercicio, si reduce la pulsación propia a wn = 80, ¿se engancha el PLL correctamente? ¿Por qué?",
              "Para comprobar si el problema es el margen de enganche, reduzca el error de frecuencia al 3 %. ¿Se engancha ahora correctamente el PLL? ¿Cual es la relación entre el margen de enganche y el ancho de banda del filtro?",
              "Construir una función en Python que genere la señal de entrada al PLL, constituida por una rampa en frecuencia: fuente fvar(f0, ffinal, Ts, faseinicial, N). Con la función que acaba de crear, genere una señal con error de fase inicial (π/2), y una rampa en frecuencia del 10 %, tomando como frecuencia inicial: f0 = 1 kHz. Vamos a tomar esta señal como entrada al PLL.",
              "Con el filtro 'rc', ajustar los parámetros del bucle a: (ξ = √2/2, wn = 450). ¿Consigue engancharse el PLL al introducir el error de frecuencia en forma de rampa?",
              "Con el filtro “lead-lag activo”, ajustar los parámetros del bucle a: (ξ = √2/2, wn = 180). ¿Se engancha correctamente el PLL? ¿Existe un error de fase constante?",
              "Repetir el ejercicio tomando: (ξ = √2/2, wn = 280). ¿Qué sucede con el error de fase del PLL? ¿Por qué?",
              "Con las consideraciones anteriores, generar y representar la señal a la salida del Generador de Código de la Figura 3, cuando generamos un número de pulsos igual a: Nd = 10.",
              "Con el procedimiento descrito representar la respuesta al impulso y la función de transferencia del filtro en coseno alzado diseñado.",
              "Obtener y dibujar la señal moduladora (xm) a la salida del filtro.",
              "Repetir el ejercicio anterior tomando un intervalo entre símbolos: Tb = 1 seg. ¿Qué ocurre cuando hay dos pulsos consecutivos? ¿Cuál sería la única forma de evitar interferencia entre símbolos en este caso? Volver al (Tb = 2 seg) para evitar interferencia entre símbolos.",
              "Obtener y dibujar la señal AM a la salida del transmisor, x (tomar índice de modulación, m = 1, y frecuencia de portadora: f0 = 1 kHz).",
              "Intentar realizar la detección coherente con el filtro “rc”, tomando los siguientes parámetros: (ξ = √2/2, wn = 120). ¿Consigue engancharse el PLL? ¿Por qué? ¿Recupera correctamente el mensaje?",
              "Repetir el intento aumentando el ancho de banda del filtro “rc”: (ξ = √2/2, wn = 220). ¿Consigue engancharse ahora el PLL? ¿Recupera correctamente el mensaje?",
              "Repetir el intento con un ancho de banda todavía mayor: (ξ = √2/2, wn = 450). ¿Consigue engancharse ahora el PLL? ¿Recupera correctamente el mensaje? ¿Por qué?",
              "Intentar realizar la detección coherente con el filtro “lead-lag activo”, tomando los siguientes parámetros: (ξ = √2/2, wn = 120). ¿Consigue engancharse el PLL?, ¿por qué? ¿Recupera correctamente el mensaje sin ning´un tipo de distorsión?"
              ]

respuestas = [
              "Se ilustran a modo de ejemplo cuatro señales sinusoidales tipo seno distintas. (A) f = 10 Hz, φ = 0, N = 1000. (B) f = 10 Hz, φ = π/2, N = 1000. (C) f = 5 Hz, φ = 0, N = 1000. (D) f = 5 Hz, φ = π/2, N = 1000.\n (E) f = 1 Hz, φ = 0, N = 1000. (F) f = 1 Hz, φ = π/2, N = 1000.",
              "El la gráfica (A) se muestra la señal de entrada al PLL. (A) f = 1000 Hz, φ = π/2, N = 1000.",
              "El la gráfica (A) se muestra la señal de entrada al PLL con un salto de fase de Δφ = π/2 en la mitad. (A) f = 1000 Hz, φ = π/2, N = 1000.",
              "Se ilustra a modo de ejemplo en la Gráfica (C) la salida del detector (multiplicador de cuatro cuadrantes) de las señales (A) f = 200 Hz, φ = π/2 y (B) f = 100 Hz, φ = 0.",
              "El la gráfica (A) se muestra la primer señal de entrada con f = 1000 Hz, φ = 0, en la gráfica (B) la segunda señal con f = 1000 Hz, φ = π/4, y en la gráfica (C) la salida del detector. Se observa que el producto es una señal oscilatoria levantada con una componente continua en torno a V = 0.354. Dicha componente viene dada por el fasaje de ambas señales",
              "El la gráfica (A) se muestra la primer señal de entrada con f = 1000 Hz, φ = 0, en la gráfica (B) la segunda señal con f = 1000 Hz, φ = π/2, y en la gráfica (C) la salida del detector. Se observa que el producto es una señal oscilatoria sin una componente continua. En este caso el detector no indica diferencia de fase.",
              "En la gráfica (A) se muestra la señal de entrada con ruido aleatorio, en (B) la salida de un filtro rc con R = C = 0.25 (es decir frecuencia angular de corte w = 16 Hz), y en (C) la salida de un filtro lead-lag activo con idénticos parámetros. En la gráfica (D) se muestra una entrada compuesta por dos senos de frecuencias f = 1 Hz y f = 12 Hz superpuestos, en (E) la salida de un filtro rc también con R = C = 0.25, y en (F) la salida de un filtro lead-lag activo con idénticos parámetros",
              "En la gráfica (A) se muestra la señal de entrada tipo pulso. En (B) la salida del filtro rc con  ξ = √2/2, wn = 2, (C) con ξ = √2/2, wn = 100 y (D) con ξ = 5, wn = 2. En cada caso la función de transferencia se obtiene pulsando sobre 'Frecuencias' para cada salida.",
              "En la gráfica (A) se muestra la señal de entrada al filtro rc formada por la salida del detector() cuando sus entradas son dos señales sinusoidales con frecuencia f = 1000 y diferencia de fase π/4 (gráficas (A) y (C)). En (D) el filtrado con  ξ = √2/2, wn = 2, (E) con ξ = √2/2, wn = 100 y (F) con ξ = 5, wn = 2.",
              "En la gráfica (A) se muestra la señal de entrada al filtro ll activo. En (B) el filtrado con  ξ = √2/2, wn = 2, (C) con ξ = √2/2, wn = 100 y (D) con ξ = 0.1, wn = 2.",
              "Con la función construida se armaron las gráficas de fase del VCO como función del tiempo (B), (D), cada una para las entradas (A) f = 10 Hz, φ = 0, N = 1000 y (C) f = 5 Hz, φ = 0, N = 1000 respectivamente.",
              "El la gráfica (A) se muestra la señal moduladora con f = 40 Hz, φ = 0, N = 1000, Ts = 0.00001. Para obtener la representación en el dominio de frecuencias pulsar sobre el botón 'frecuencia'.",
              "En la gráfica (A) se muestra la señal moduladura con f = 40 Hz, φ = 0, N = 1000, Ts = 0.00001. En la gráfica (B) la salida del VCO con K = 0. Para obtener la representación en el dominio de frecuencias pulsar sobre el botón 'frecuencia'.",
              "En la gráfica (A) se muestra la señal moduladura con f = 40 Hz, φ = 0, N = 1000, Ts = 0.00001. En la gráfica (B) la salida del VCO con K = 100. Para obtener la representación en el dominio de frecuencias pulsar sobre el botón 'frecuencia'.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. Dicha señal se pasó a través de la función PLL con wn = 180. En la gráfica (B) se muestra la salida con ξ = √2/2, en la gráfica (C) con ξ = 0.3 y en la gráfica (D) con ξ = 2.0.",
              "En la gráfica (A) se muestra el diagrama de lissajous entre la entrada y la salida del PLL con ξ = √2/2, mientras que en la gráfica (B) se muestra la señal error para dichas señales. Análogamente en las gráficas (C) y (D) se muestran las gráficas de lissajous y de error para ξ = 0.3, y finalmente en las gráficas (E) y (F) para ξ = 2.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muesta la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO).",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muesta la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). Se observa un comportamiento similar que en el anterior ejemplo.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas. El PLL no engancha con la frecuencia dada.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas. Según se observa, no se consigue enganchar el PLL.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas. Según se observa, no se consigue enganchar el PLL.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas. Según se observa, no se consigue enganchar el PLL al introducirse un error de fase.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas. Según se observa, no se consigue enganchar el PLL.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas. Según se observa, no se consigue enganchar el PLL al introducir el error en frecuencia",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida del detector de fase. En la gráfica (C) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (D) se encuentra la salida del PLL (es decir del VCO). En la gráfica (E) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (F) está la señal de error entre ambas. Se aprecia que el PLL engancha con la señal de entrada.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas. Según se observa, no se consigue enganchar el PLL.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas. El error de fase del PLL se reduce hasta enganchar el PLL en el cual oscila relativamente poco con respecto a la fase dada.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a unir dos señales sinusoidales defasadas. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a una sinusoidal cuya frecuencia tiene un error. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a una sinusoidal cuya frecuencia tiene un error. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a una sinusoidal cuya frecuencia tiene un error. En la gráfica (B) se muestra la salida que se obtiene del filtro del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas.",              
              "En la gráfica (A) se muestra la señal de entrada generada en base a una rampa de frecuencia desde f = 1000 Hz hasta f  = 1100 Hz.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a una rampa de frecuencia desde f = 1000 Hz hasta f  = 1100 Hz. En la gráfica (B) se muestra la salida que se obtiene del filtro rc del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a una rampa de frecuencia desde f = 1000 Hz hasta f  = 1100 Hz. En la gráfica (B) se muestra la salida que se obtiene del filtro lead-lag activo del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a una rampa de frecuencia desde f = 1000 Hz hasta f  = 1100 Hz. En la gráfica (B) se muestra la salida que se obtiene del filtro lead-lag activo del PLL al pasar la señal en (A) como entrada. En la gráfica (C) se encuentra la salida del PLL (es decir del VCO). En la gráfica (D) se muestra el diagrama de lissajous entre la entrada y la salida, mientras que en la gráfica (E) está la señal de error entre ambas.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a la función gen_cod, y que contiene 10 pulsos binarios espaciados cada 2 segundos.",
              "En la gráfica (A) se muestra la respuesta del filtro tipo coseno alzado.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a la función gen_cod, y que contiene 10 pulsos binarios espaciados cada 2 segundos. En la gráfica (B) se muestra el resultado de convolucionar numéricamente dicha señal con la respuesta al filtro tipo coseno alzado con Tb = 2.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a la función gen_cod, y que contiene 10 pulsos binarios espaciados cada 2 segundos. En la gráfica (B) se muestra el resultado de convolucionar numéricamente dicha señal con la respuesta al filtro tipo coseno alzado con Tb = 1.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a la función gen_cod, y que contiene 10 pulsos binarios espaciados cada 2 segundos. En la gráfica (B) se muestra el resultado de convolucionar numéricamente dicha señal con la respuesta al filtro tipo coseno alzado con Tb = 2. En la gráfica (C) se muestra la señal moduladora y finalmente en la gráfica (D) el resultado de combinar la señal con la moduladora (es decir la salida de la emisora).",
              "En la gráfica (A) se muestra la señal de entrada generada en base a la función gen_cod, y que contiene 10 pulsos binarios espaciados cada 2 segundos. En la gráfica (B) la salida de la emisora con dicha señal filtrada y modulada. En la gráfica (C) se muestra la salida del filtro rc del PLL del receptor. En la gráfica (D) se tiene la salida del PLL (es decir del VCO), y finalmente en la gráfica (E) el resultado de combinar dicha señal con la entrada y filtrarla con un conseno alzado.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a la función gen_cod, y que contiene 10 pulsos binarios espaciados cada 2 segundos. En la gráfica (B) la salida de la emisora con dicha señal filtrada y modulada. En la gráfica (C) se muestra la salida del filtro rc del PLL del receptor. En la gráfica (D) se tiene la salida del PLL (es decir del VCO), y finalmente en la gráfica (E) el resultado de combinar dicha señal con la entrada y filtrarla con un conseno alzado.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a la función gen_cod, y que contiene 10 pulsos binarios espaciados cada 2 segundos. En la gráfica (B) la salida de la emisora con dicha señal filtrada y modulada. En la gráfica (C) se muestra la salida del filtro rc del PLL del receptor. En la gráfica (D) se tiene la salida del PLL (es decir del VCO), y finalmente en la gráfica (E) el resultado de combinar dicha señal con la entrada y filtrarla con un conseno alzado.",
              "En la gráfica (A) se muestra la señal de entrada generada en base a la función gen_cod, y que contiene 10 pulsos binarios espaciados cada 2 segundos. En la gráfica (B) la salida de la emisora con dicha señal filtrada y modulada. En la gráfica (C) se muestra la salida del filtro lead-lag activo del PLL del receptor. En la gráfica (D) se tiene la salida del PLL (es decir del VCO), y finalmente en la gráfica (E) el resultado de combinar dicha señal con la entrada y filtrarla con un conseno alzado.",
              ]

"""
"Generar ahora una señal de entrada al PLL con el error de fase inicial de π/2, y un error de
frecuencia del 10 %. Representar en cada caso la señal de error y el diagrama de Lissajous."
"""