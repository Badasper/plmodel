# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:32:18 2018
@author: Yakovlev Alexander
"""

import numpy as np


__version__ = '1.0'
__author__ = 'Yakovlev Alexander'


def to_db(value):
    return 10 * np.log10(value)


def from_db(value_in_db):
    return 10**(value_in_db / 10)


def convert_rad_to_deg(radians):
    return radians * 180 / np.pi


def convert_deg_to_rad(degree):
    return degree * np.pi / 180


def interpolate_log_xp(xp, yp, num):
    if not (xp or yp):
        return np.array([]), np.array([])
    xp = to_db(np.array(xp))
    x_interp = np.linspace(min(xp), max(xp), num=num)
    return from_db(x_interp),  np.interp(x_interp, xp, yp)


def calc_rms_rad(freq, dbc, fstart=None, fstop=None,):
    # TODO edge of integration fstart to fstop
    return np.sqrt(2 * np.trapz(from_db(dbc), freq))


def calc_interp_rms_rad(freq, dbc, num):
    freq_interp, dbc_interp = interpolate_log_xp(freq, dbc, num)
    return calc_rms_rad(freq_interp, dbc_interp)


def dbm_to_dbw(value):
    return value - 30


def dbw_to_dbm(value):
    return value + 30


def dbm_to_watt(value):
    return 10 ** (dbm_to_dbw(value) / 10)


def dbw_to_watt(value):
    return 10 ** (value / 10)


def watt_to_dbm(watt):
    if watt <= 0:
        raise ValueError("Power <= 0 W")
    return dbw_to_dbm(10 * np.log10(watt))


def watt_to_dbw(watt):
    """
    Convert Watt to dBw 10*log10(Power_in_watt)
    :param watt: float
    :return: float
    """
    if watt <= 0:
        raise ValueError("Power <= 0 W")
    return 10 * np.log10(watt)


def rss(data=None):
    """
    :param data: iterable (lst, tuple, ndarray)
    :return: ndarray, root sum of the squares:
    """
    if data is None:
        data = np.array([])
    squares = np.square(np.array(data))
    sum_square = squares.sum(axis=0)
    return np.sqrt(sum_square)