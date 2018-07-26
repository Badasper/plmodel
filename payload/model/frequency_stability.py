# -*- coding: utf-8 -*-
"""
Created on 11/05/18
@author: Yakovlev Alexander
"""

from payload.rf_calc.rfutil import rss


class FrequencyStability:
    def __init__(self, LO, ppm):
        self._lo = LO
        self._ppm = ppm

    def calc_offset(self):
        return self._lo * self._ppm * 10**-6


class ChainFrequencyStability:
    def __init__(self, frequency_stability_lst=None):
        if frequency_stability_lst is None:
            frequency_stability_lst = []
        self._fs_lst = frequency_stability_lst

    def append(self, freq_stability):
        self._fs_lst.append(freq_stability)
        return 0

    def calc_offset(self):
        frequencies_offsets = [x.calc_offset() for x in self._fs_lst]
        return rss(frequencies_offsets)

    def calc_offset_worst(self):
        return sum([val.calc_offset() for val in self._fs_lst])
