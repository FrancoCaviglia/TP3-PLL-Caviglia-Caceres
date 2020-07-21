# -*- coding: utf-8 -*-

import numpy as np
from numpy.random import randn
from scipy.signal import lfilter, lfilter_zi, filtfilt, butter
from matplotlib.pyplot import plot, legend, show, grid, figure, savefig

# Generate a noisy signal to be filtered.
t = np.linspace(-1, 1, 201)
x = (np.sin(2*np.pi*0.75*t*(1-t)+2.1)+0.1*np.sin(2*np.pi*1.25*t +1)+0.18*np.cos(2*np.pi*3.85*t))
xn = x + randn(len(t))*0.08
# Create an order 3 lowpass butterworth filter.
b, a = butter(1, 0.03, 'lowpass', False, 'ba')

print(b, a)
# Apply the filter to xn  Use lfilter_zi to choose the initial condition
# of the filter.
zi = lfilter_zi(b, a)
z, _ = lfilter(b, a, xn, zi=zi*xn[0])
# Apply the filter again, to have a result filtered at an order
# the same as filtfilt.
z2, _ = lfilter(b, a, z, zi=zi*z[0])
# Use filtfilt to apply the filter.
y = filtfilt(b, a, xn)
# Make the plot.
figure(figsize=(10,5))
#hold(True)
plot(t, xn, 'b', linewidth=1.75, alpha=0.75)
plot(t, z, 'r--', linewidth=1.75)
plot(t, z2, 'r', linewidth=1.75)
plot(t, y, 'k', linewidth=1.75)
legend(('noisy signal','lfilter, once','lfilter, twice','filtfilt'), loc='best')
#hold(False)
grid(True)
show()
#savefig('plot.png', dpi=65)