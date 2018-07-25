# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:32:18 2018
@author: Yakovlev Alexander
"""

import numpy as np

from rf_calc.rfutil import calc_rms_rad,\
                    calc_interp_rms_rad,\
                    rad_to_deg,\
                    rss


__version__ = '1.0'
__author__ = 'Yakovlev Alexander'


class RfChain:
    def __init__(self):
        self._nodes = []


class PhaseNoise:
    points_for_integrate = 650

    def __init__(self, frequency, dbc):
        self._frequency = np.array(frequency)
        self._dbc = np.array(dbc)

    def __str__(self):
        freq = self.get_frequency_array()
        dbc = self.get_dbc_array()
        return 'frequency={}, dbc={}'.format(freq, dbc)

    def __eq__(self, other):
        frequency_equal = np.array_equal(self.get_frequency_array(), other.get_frequency_array())
        dbc_equal = np.array_equal(self.get_dbc_array(), other.get_dbc_array())
        return frequency_equal and dbc_equal

    def __ne__(self, other):
        return not (self == other)

    def set_points_for_integrate(self, points):
        self.points_for_integrate = points

    def calc_rms_rad(self, limit=None):
        if len(self._frequency) > self.points_for_integrate:
            return calc_rms_rad(self._frequency, self._dbc, limit=limit)
        return calc_interp_rms_rad(self._frequency, self._dbc, self.points_for_integrate, limit=limit)

    def calc_rms_deg(self, limit=None):
        rms_rad = self.calc_rms_rad(limit=limit)
        return rad_to_deg(rms_rad)

    def get_frequency_array(self):
        return self._frequency

    def get_dbc_array(self):
        return self._dbc


class ChainPhaseNoise(RfChain):

    def append(self, pn):
        self._nodes.append(pn)

    def calc_chain_rms_rad(self, limit=None):
        rms_rads = [x.calc_rms_rad(limit=limit) for x in self._nodes]
        return rss(rms_rads)

    def calc_chain_rms_deg(self, limit=None):
        rms_rad = self.calc_chain_rms_rad(limit=limit)
        return rad_to_deg(rms_rad)
