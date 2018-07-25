# -*- coding: utf-8 -*-
"""
Created on %(date)s
@author: Yakovlev Alexander
"""
import matplotlib.pyplot as plt
import numpy as np
from rf_calc import rfutil as rf

station_power = np.array([x for x in range(10, 500, 1)])
station_gain = np.array([x for x in range(20, 70, 10)])
eirp_tx = np.array([rf.eirp(station_power, gain) for gain in station_gain])
pfd = rf.pfd(eirp_tx, 42000000)
gain_vs_minfreq = (38.8, 5.725 * 10 ** 9)
gain_vs_maxfreq = (40, 7.725 * 10 ** 9)
prx_minfrq =  rf.dbw_to_dbm(rf.power_rx(pfd, gain_vs_minfreq))
prx_maxfreq = rf.dbw_to_dbm(rf.power_rx(pfd, gain_vs_maxfreq))
for item in prx_minfrq:
    plt.plot(station_power, item)
for item in prx_maxfreq:
    plt.plot(station_power, item)
plt.grid(which='both',linestyle="--")
plt.title('Prx')
plt.xlabel('Station Power, W')
plt.ylabel('Prx, dBm')
plt.legend()
print(prx_minfrq.min(), prx_minfrq.max(), prx_minfrq.mean())
plt.show()