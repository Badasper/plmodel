# -*- coding: utf-8 -*-
"""
Created on 11/05/18
@author: Yakovlev Alexander
"""

from ..rfutil import dbm_to_dbw


class FrequencyStability:

    def __init__(self, ppm=0):
        if ppm < 0:
            raise ValueError('ppm must be positive')
        self._parts_per_hz = ppm * 10**-6

    def get_freq_offset(self, frequency):
        return frequency * self._parts_per_hz
