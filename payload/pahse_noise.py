# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:32:18 2018
@author: Yakovlev Alexander
"""

from .rfutil import calc_rms_rad,\
                         calc_interp_rms_rad,\
                         convert_rad_to_deg


__version__ = '1.0'
__author__ = 'Yakovlev Alexander'


class PhaseNoise:
    min_points_for_integrate = 1000

    def __init__(self, frequency, dbc):
        self._frequency = frequency
        self._dbc = dbc

    def calc_rms_rad(self, fstart=None, fstop=None, points=None):
        if points is None:
            points = self.min_points_for_integrate
        if len(self._frequency) > points:
            return calc_rms_rad(self._frequency, self._dbc, fstart=fstart, fstop=fstop)
        return calc_interp_rms_rad(self._frequency, self._dbc, points)

    def calc_rms_deg(self, fstart=None, fstop=None, points=None):
        rms_rad = self.calc_rms_rad(fstart=fstart, fstop=fstop, points=points)
        return convert_rad_to_deg(rms_rad)
