# -*- coding: utf-8 -*-
"""
Created on 10/07/18
@author: Yakovlev Alexander
"""
from rf_calc.rfutil import get_interpolated_data


class BaseMeasurement:
    code = 'Base'

    def __init__(self, data):
        self._data = data


class GainResponse(BaseMeasurement):
    code = 'GF'

    def get_response(self, signal):
        frequency = signal.get_frequency()
        gain = get_interpolated_data(frequency, self._data)
        signal.apply(gain)
        return signal


class GroupDelayResponse(BaseMeasurement):
    code = 'GD'
    pass


class Measurement:
    """Adapter"""

    def __init__(self, measurement_code):
        self._measurement_code = measurement_code

    def get_measurement(self, signal, data):
        return self._measurement_code(data).get_response(signal)
