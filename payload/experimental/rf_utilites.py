import numpy as np


def to_db(value):
    return 10 * np.log10(value)


def from_db(value_in_db):
    return 10**(value_in_db / 10)


def convert_rad_to_deg(radians):
    return radians * 180 / np.pi


def convert_deg_to_rad(degree):
    return degree * np.pi / 180


def interpolate_log_x(xp, yp, num):
    if not (xp or yp):
        return np.array([]), np.array([])
    xp = to_db(np.array(xp))
    x_interp = np.linspace(min(xp), max(xp), num=num)
    return from_db(x_interp),  np.interp(x_interp, xp, yp)


def calc_rms_rad(freq, dbc, fstart=None, fstop=None,):
    # TODO edge of integration fstart to fstop
    return np.sqrt(2 * np.trapz(from_db(dbc), freq))


def calc_interp_rms_rad(freq, dbc, num):
    freq_interp, dbc_interp = interpolate_log_x(freq, dbc, num)
    return calc_rms_rad(freq_interp, dbc_interp)
