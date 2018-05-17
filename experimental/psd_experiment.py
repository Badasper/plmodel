# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: Yakovlev Alexander
"""
import matplotlib.pyplot as plt
import numpy as np
from payload import rfutil as rf


station_power = np.array([x for x in range(10, 200, 1)])
station_gain = np.array([x for x in range(20, 70, 10)])
eirp_tx = np.array([rf.eirp(station_power, gain) for gain in station_gain])
pfd = rf.pfd(eirp_tx, 42000000)
gain_vs_wavelength = (38.8, 0.045)
prx = rf.dbw_to_dbm(rf.power_rx(pfd, gain_vs_wavelength))

for item in prx:
    plt.plot(station_power, item)
plt.grid(which='both',linestyle="--")
plt.title('Prx')
plt.xlabel('Station Power, W')
plt.ylabel('Prx, dBW')
plt.legend([' '.join([str(x), 'dB']) for x in station_gain])
print(prx.min(), prx.max(), prx.mean())
plt.show()