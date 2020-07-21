# -*- coding: utf-8 -*-

from scipy import signal
import numpy as np

w0 = 1000
fs = 100
#print( signal.butter(1, w0, btype='lowpass', analog=True, output='ba') )
for i in np.arange(0.0001,0.99,0.01):
    
    """ Para el filtro RC pasa-bajo """ 
    
    coef = signal.butter(1, i, btype='lowpass', analog=True, output='ba')#, fs)
    print(coef)
    print((np.array([i]),np.array([1,i])))
    print(signal.bilinear(coef[0],coef[1]))
#    print('Trans s: ',np.abs(signal.freqs(coef[0], coef[1], i)[1][0]) )
#    print('Trans z: ',np.abs(signal.freqz(coef[0], coef[1], i)[1][0]) )
#    print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
    coef = signal.butter(1, i, btype='lowpass', analog=False, output='ba')#, fs)
    print(coef)
    print(signal.bilinear(coef[0],coef[1]))
    #print('Trans s: ',np.abs(signal.freqs(coef[0], coef[1], i)[1][0]) )
#   print('Trans z: ',np.abs(signal.freqz(coef[0], coef[1], i)[1][0]) )
#   print('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    #print(signal.bilinear([1], [1, i]))
    print(signal.bilinear([1], [1/i, 1]))
    #print(np.array([1/(1-2*i),1/(1-2*i)]), np.array([1,(1+2*i)/(1-2*i)]))
    print((np.array([1/(1+2*(1/i)),1/(1+2*(1/i))]), np.array([1,(1-2*(1/i))/(1+2*(1/i))])))
#    print('Trans s: ',np.abs(signal.freqs([1], [1/i, 1], i)[1][0]) )
#    print('Trans z: ',np.abs(signal.freqz([1], [1/i, 1], i)[1][0]) )
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')