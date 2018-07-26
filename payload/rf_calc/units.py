# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:32:18 2018
@author: Yakovlev Alexander
"""

from payload.rf_calc import rfutil


class Units:
    """
    Physic units_tool
    """
    main_units = "unit"

    def __init__(self, value=0.0, units=None):
        self.units_set = self._get_dict_of_units()
        if units is None:
            self._value = float(value)
        else:
            self._value = self._convert_to_main_units(value, units)

    def __str__(self):
        return "{} {}".format(self._value, self.main_units)

    def __repr__(self):
        return "{} {}.".format(self._value, self.main_units)

    def _get_dict_of_units(self):
        return {
            self.main_units: 1,
            "p" + self.main_units: 10**-12,
            "n" + self.main_units: 10**-9,
            "u" + self.main_units: 10**-6,
            "m" + self.main_units: 10**-3,
            "k" + self.main_units: 10**3,
            "M" + self.main_units: 10**6,
            "G" + self.main_units: 10**9,
            "T" + self.main_units: 10**12
        }

    def _get_coefficient(self, units=None):
        if units not in self.units_set:
            pattern = "non-{} unit, check please entry data!"
            raise ValueError(pattern.format(units))
        return self.units_set[units]

    def _convert_to_main_units(self, value, units):
        return float(value) * self._get_coefficient(units)

    def get_value(self, units=None):
        if units:
            return self._value / self._get_coefficient(units)
        return self._value

    def get_units(self):
        return self.main_units


class Frequency(Units):
    main_units = "Hz"

    def __add__(self, other):
        return Frequency(self.get_value() + other.get_value())

    def __sub__(self, other):
        return Frequency(self.get_value() - other.get_value())


class Power(Units):
    main_units = "W"


class PowerLog(Power):
    def get_value(self, units=None):
        if not units:
            return self._value
        if units in ("dBm", "dBW"):
            return self._get_coefficient(units)(self._value)
        value_in_watt = rfutil.dbm_to_watt(self._value)
        return value_in_watt / self._get_coefficient(units)

    def _convert_to_main_units(self, value, units):
        if units in ("dBm", "dBW"):
            return self._get_coefficient(units)(value)
        value = super()._convert_to_main_units(value, units)
        return rfutil.watt_to_dbm(value)

    def _get_dict_of_units(self):
        dict_out = super()._get_dict_of_units()
        dict_out.update({"dBm": lambda x: x, "dBW": rfutil.dbm_to_dbw})
        self.main_units = "dBm"
        return dict_out


class Temperature(Units):
    main_units = "C"


class Pressure(Units):
    main_units = "Pa"


class Second(Units):
    main_units = "s"


class Gramm(Units):
    main_units = "g"
