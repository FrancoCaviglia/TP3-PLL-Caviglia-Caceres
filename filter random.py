from scipy import zeros, signal, random
import matplotlib.pyplot as plt

def filter_sbs():
    data = random.random(2000)
    b = signal.firwin(150, 0.004)
    z = signal.lfilter_zi(b, 1)
    result = zeros(data.size)
    for i, x in enumerate(data):
        result[i], z = signal.lfilter(b, 1, [x], zi=z)
    return result, data

plt.figure()
plt.plot(filter_sbs()[0], 'r') # Azul
plt.show()

plt.figure()
plt.plot(filter_sbs()[1], 'b') # Azul
plt.show()