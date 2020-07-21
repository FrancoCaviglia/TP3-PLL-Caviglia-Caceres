# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

alpha = 0.35

freq_vco = 1.0
freq_in = 8
offset = 0

dl_i = [0]*32
dl_q = [0]*32
dl_o = [0]*32

sincf = np.sinc(np.arange(-np.pi, np.pi, np.pi/16))

ts = np.arange(0, np.pi*8, np.pi/1000)

pll_ins = []
pll_outs = []
fs = []

for t in ts:
    vco_i = np.sin(t*(freq_vco + offset)*np.pi*2)
    vco_q = np.cos(t*(freq_vco + offset)*np.pi*2)
    pll_in = np.sin(t*freq_in*np.pi*2)

    dl_i = dl_i[1:]
    dl_q = dl_q[1:]
    dl_o = dl_o[1:]

    dl_i = [vco_i*pll_in] + dl_i
    dl_q = [vco_q*pll_in] + dl_q

    o_i = np.sum(sincf*dl_i)
    o_q = np.sum(sincf*dl_q)

    dl_o = [o_i+o_q] + dl_o
    f = np.sum(sincf*dl_o)
    offset += f*alpha

    pll_out = vco_i

    pll_ins.append(pll_in)
    pll_outs.append(pll_out)
    fs.append(f)

plt.plot(pll_ins)
plt.plot(pll_outs)
plt.plot(fs)
plt.show()