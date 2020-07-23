# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

""" E """
tn_1 = [0.20, 0.05, 0.05, 0.20, 0.05, 0.05, 0.20]
xn_1 = [0.90, 0.90, 0.50, 0.50, 0.50, 0.10, 0.10]
""" X """
tn_2 = [0.25, 0.45]
xn_2 = [0.10, 0.90]
tn_3 = [0.45, 0.25]
xn_3 = [0.10, 0.90]
""" P """
tn_4 = [0.5, 0.5, 0.7, 0.7, 0.5]
xn_4 = [0.1, 0.9, 0.9, 0.5, 0.5]
""" E """
tn_5 = [0.95, 0.80, 0.80, 0.95, 0.80, 0.80, 0.95]
xn_5 = [0.90, 0.90, 0.50, 0.50, 0.50, 0.10, 0.10]
""" I """
tn_6 = [0.100, 0.450, 0.275, 0.275, 0.450, 0.100]
xn_6 = [0.100, 0.100, 0.100, 0.900, 0.900, 0.900]
""" I """
tn_7 = [0.600, 0.950, 0.775, 0.775, 0.950, 0.600]
xn_7 = [0.100, 0.100, 0.100, 0.900, 0.900, 0.900]
""" I """
tn_8 = [0.050, 0.400, 0.225, 0.225, 0.400, 0.050]
xn_8 = [0.100, 0.100, 0.100, 0.900, 0.900, 0.900]
""" . """
tn_9 = [0.450, 0.450, 0.500, 0.500, 0.450]
xn_9 = [0.100, 0.200, 0.200, 0.100, 0.100]
""" B """
tn_10 = [0.60, 0.60, 0.80, 0.85, 0.85, 0.80, 0.60, 0.80, 0.85, 0.85, 0.80, 0.60]
xn_10 = [0.10, 0.90, 0.90, 0.80, 0.65, 0.50, 0.50, 0.50, 0.35, 0.20, 0.10, 0.10]
""" . """
tn_11 = [0.900, 0.900, 0.950, 0.950, 0.900]
xn_11 = [0.100, 0.200, 0.200, 0.100, 0.100]

def caratula_1():

    car_1 = plt.figure()
    
    plt.plot(tn_1, xn_1, 'b', linewidth=7.0)
    plt.plot(tn_2, xn_2, 'b', linewidth=7.0)
    plt.plot(tn_3, xn_3, 'b', linewidth=7.0)
    plt.plot(tn_4, xn_4, 'b', linewidth=7.0)
    plt.plot(tn_5, xn_5, 'b', linewidth=7.0)

    plt.grid()
    plt.tight_layout()
    
    return car_1

def caratula_2():
    
    car_2 = plt.figure()

    plt.plot(tn_6, xn_6, 'g', linewidth=7.0)
    plt.plot(tn_7, xn_7, 'g', linewidth=7.0)

    plt.grid()
    plt.tight_layout()
    
    return car_2

def caratula_3():
   
    car_3 = plt.figure()

    plt.plot(tn_8, xn_8, 'r', linewidth=7.0)
    plt.plot(tn_9, xn_9, 'r', linewidth=7.0)
    plt.plot(tn_10, xn_10, 'r', linewidth=7.0)
    plt.plot(tn_11, xn_11, 'r', linewidth=7.0)

    plt.grid()
    plt.tight_layout()
    
    return car_3