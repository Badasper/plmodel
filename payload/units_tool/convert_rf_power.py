import numpy as np


def dbm_to_dbw(value):
    return value - 30


def dbw_to_dbm(value):
    return value + 30


def dbm_to_watt(value):
    return 10 ** (dbm_to_dbw(value) / 10)


def dbw_to_watt(value):
    return 10 ** (value / 10)


def watt_to_dbm(value):
    if value <= 0:
        raise ValueError("Power <= 0 W")
    return dbw_to_dbm(10 * np.log10(value))


def watt_to_dbw(value):
    if value <= 0:
        raise ValueError("Power <= 0 W")
    return 10 * np.log10(value)
