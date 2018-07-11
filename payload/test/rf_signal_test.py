# -*- coding: utf-8 -*-
from model.rf_signal import RadioSignal
from rf_calc.phase_noise import PhaseNoise


class TestCaseRadioSignal:

    def test_signal_info(self):
        rf = RadioSignal('test_cw',
                         center_frequency=1000,
                         bandwidth=10)
        rf.append_trace(source='Generator')
        assert rf.get_source() == 'Generator'
        assert rf.get_label() == 'test_cw'
        assert str(rf) == 'test_cw: CF=1000.0 MHz, BW=10.0 MHz'

    def test_signal_get_frequency(self):
        rf = RadioSignal('test_cw',
                         center_frequency=1000,
                         bandwidth=10)
        actual_cf = rf.get_cf_frequency(units='MHz')
        actual_cf_hz = rf.get_cf_frequency(units='Hz')
        assert actual_cf == 1000.0
        assert actual_cf_hz == 1000000000.0
        actual_bw = rf.get_bw_frequency(units='MHz')
        assert actual_bw == 10.0

    def test_signal_history(self):
        rf = RadioSignal('test_cw',
                         center_frequency=1000,
                         bandwidth=10)
        rf.append_trace(source='Generator')
        assert rf.trace() == [{'source': 'Generator',
                               'center_frequency': 1000000000.0,
                               'bandwidth': 10000000.0,
                               'power': None,
                               'phase': 0,
                               'phase_noise': PhaseNoise([], [])
                               }, ]
        rf.append_trace(source='The_next_block')
        assert rf.trace() == [{'source': 'Generator',
                               'center_frequency': 1000000000.0,
                               'bandwidth': 10000000.0,
                               'power': None,
                               'phase': 0,
                               'phase_noise': PhaseNoise([], [])
                               },
                              {'source': 'The_next_block',
                               'center_frequency': 1000000000.0,
                               'bandwidth': 10000000.0,
                               'power': None,
                               'phase': 0,
                               'phase_noise': PhaseNoise([], [])
                               }, ]

    def test_signal_convert(self):
        rf = RadioSignal('test_cw',
                         center_frequency=1000,
                         bandwidth=10)
        rf.convert_frequency(local_oscillator_freq=200, units='MHz')
        rf.append_trace(source='conv1')
        assert rf.get_cf_frequency(units='MHz') == 1200.0
        rf.convert_frequency(local_oscillator_freq=-300, units='MHz')
        rf.append_trace(source='conv2')
        assert rf.get_cf_frequency(units='MHz') == 900.0
        rf.convert_frequency(local_oscillator_freq=-1200, units='MHz')
        rf.append_trace(source='conv3')
        assert rf.get_cf_frequency(units='MHz') == -300.0

    def test_signal_power(self):
        rf = RadioSignal('test_cw',
                         center_frequency=1000,
                         bandwidth=10)
        rf.set_power(-10, units='dBm')
        rf.append_trace(source='Generator')
        assert rf.get_power(units='dBm') == -10.0
        rf.set_power(-20, units='dBm')
        assert rf.get_power(units='dBm') == -20.0
        rf.apply_gain(20)
        rf.append_trace(source='LNA')
        assert rf.get_power(units='dBm') == 0.0
        assert rf.get_power(units='dBW') == -30.0

    def test_signal_phase_noise(self):
        rf = RadioSignal('test_cw',
                         center_frequency=1000,
                         bandwidth=10)
        rf.add_phase_noise(PhaseNoise([10, 100], [-40, -50]))
