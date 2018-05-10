# -*- coding: utf-8 -*-
#
from units_tool.units import Frequency, PowerLog


class RadioSignal:

    def __init__(self, label, center_frequency=None, bandwidth=None, units='MHz'):
        self._label = label
        if center_frequency is None:
            self._center_freq = Frequency(0, units=units)
        if bandwidth is None:
            self._bandwidth_freq = Frequency(0, units=units)
        self._center_freq = Frequency(center_frequency, units=units)
        self._bandwidth_freq = Frequency(bandwidth, units=units)
        self._source = ''
        self._trace = []
        self._power = None

    def __str__(self):
        return '{}: CW={} MHz, BW={} MHz'.format(self.get_label(),
                                                 self.get_cf_frequency(units='MHz'),
                                                 self.get_bw_frequency(units='MHz'))

    def _set_source(self, source):
        self._source = source

    def set_power(self, value, units):
        self._power = PowerLog(value, units=units)

    def get_power(self, units):
        if self._power is not None:
            return self._power.get_value(units=units)

    def get_source(self):
        return self._source

    def get_label(self):
        return self._label

    def get_bw_frequency(self, units='Hz'):
        return self._bandwidth_freq.get_value(units=units)

    def get_cf_frequency(self, units='Hz'):
        return self._center_freq.get_value(units=units)

    def append_trace(self, *, source):
        self._set_source(source)
        node = {'source': self.get_source(),
                'center_frequency': self.get_cf_frequency(),
                'bandwidth': self.get_bw_frequency(),
                'power': self.get_power(units='dBm'),
                'phase': 0
                }
        self._trace.append(node)

    def trace(self):
        return self._trace

    def convert_frequency(self, *, local_oscillator_freq, units='MHz'):
        self._center_freq = Frequency(local_oscillator_freq, units=units) + self._center_freq

    def apply_gain(self, gain=0):
        prev_power = self.get_power(units='dBm')
        self._power = PowerLog(prev_power + gain, units='dBm')