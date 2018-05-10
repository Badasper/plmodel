#!/usr/bin/env python3


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
            "p" + self.main_units: 10 ** -12,
            "n" + self.main_units: 10 ** -9,
            "u" + self.main_units: 10 ** -6,
            "m" + self.main_units: 10 ** -3,
            "k" + self.main_units: 10 ** 3,
            "M" + self.main_units: 10 ** 6,
            "G" + self.main_units: 10 ** 9,
            "T" + self.main_units: 10 ** 12
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
