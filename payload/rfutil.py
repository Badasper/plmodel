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


def from_db(db):
    return 10**(db / 10)


def rad_to_deg(radians):
    return radians * 180 / np.pi


def deg_to_rad(degree):
    return degree * np.pi / 180


def dbm_to_dbw(dbm):
    return dbm - 30


def dbw_to_dbm(dbw):
    return dbw + 30


def dbm_to_watt(dbm):
    return from_db(dbm_to_dbw(dbm))


def dbw_to_watt(dbw):
    return from_db(dbw)


def watt_to_dbw(watt):
    return to_db(watt)


def watt_to_dbm(watt):
    return dbw_to_dbm(watt_to_dbw(watt))


def interpolate_log_xp(xp, yp, num):
    if not (xp.any() or yp.any()):
        return np.array([]), np.array([])
    xp = to_db(xp)
    x_interp = np.linspace(xp.min(), xp.max(), num=num)
    return from_db(x_interp),  np.interp(x_interp, xp, yp)


def get_nearest_idx(value, array):
    return (np.abs(array - value)).argmin()


def get_limited_data_x_y(x, y, limit):
    x_min = limit[0]
    x_max = limit[1]
    idx_min = get_nearest_idx(x_min, x)
    idx_max = get_nearest_idx(x_max, x)
    x = x[idx_min:idx_max]
    y = y[idx_min:idx_max]
    return x, y


def calc_integrated_phase_noise(freq, power_w):
    return np.sqrt(2 * np.trapz(power_w, freq))


def calc_rms_rad(freq, dbc, limit=None):
    power_w = from_db(dbc)
    if limit:
        freq, power_w = get_limited_data_x_y(freq, power_w, limit)
    return calc_integrated_phase_noise(freq, power_w)


def calc_interp_rms_rad(freq, dbc, num, limit=None):
    freq_interp, dbc_interp = interpolate_log_xp(freq, dbc, num)
    return calc_rms_rad(freq_interp, dbc_interp, limit=limit)


def rss(data=None):
    if data is None:
        data = np.array([])
    squares = np.square(data)
    sum_square = squares.sum(axis=0)
    return np.sqrt(sum_square)
