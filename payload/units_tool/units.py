from .base_units import Units

from . import convert_rf_power


class Temperature(Units):
    main_units = "C"


class Pressure(Units):
    main_units = "Pa"


class Second(Units):
    main_units = "s"


class Gramm(Units):
    main_units = "g"


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
        value_in_watt = convert_rf_power.dbm_to_watt(self._value)
        return value_in_watt / self._get_coefficient(units)

    def _convert_to_main_units(self, value, units):
        if units in ("dBm", "dBW"):
            return self._get_coefficient(units)(value)
        value = super()._convert_to_main_units(value, units)
        return convert_rf_power.watt_to_dbm(value)

    def _get_dict_of_units(self):
        dict_out = super()._get_dict_of_units()
        dict_out.update({
            "dBm": lambda x: x,
            "dBW": convert_rf_power.dbm_to_dbw
        })
        self.main_units = "dBm"
        return dict_out
