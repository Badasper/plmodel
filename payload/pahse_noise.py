# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:32:18 2018
@author: Yakovlev Alexander
"""

import numpy as np

from .rfutil import calc_rms_rad,\
                    calc_interp_rms_rad,\
                    convert_rad_to_deg


__version__ = '1.0'
__author__ = 'Yakovlev Alexander'


class PhaseNoise:
    min_points_for_integrate = 700

    def __init__(self, frequency, dbc):
        self._frequency = np.array(frequency)
        self._dbc = np.array(dbc)

    def calc_rms_rad(self, limit=None, points=None):
        if points is None:
            points = self.min_points_for_integrate
        if len(self._frequency) > points:
            return calc_rms_rad(self._frequency, self._dbc, limit=limit)
        return calc_interp_rms_rad(self._frequency, self._dbc, points, limit=limit)

    def calc_rms_deg(self, limit=None, points=None):
        rms_rad = self.calc_rms_rad(limit=limit, points=points)
        return convert_rad_to_deg(rms_rad)
