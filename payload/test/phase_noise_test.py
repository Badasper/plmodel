import os
from ..experimental.pahse_noise import PhaseNoise


class TestCasePhaseNoise:

    def test_calc_rms_deg(self):
        frequency = [10**x for x in range(1, 8)]
        phase_noise_spec = [-38, -66, -78, -87, -93, -95, -115]
        dbc = [x-6 for x in phase_noise_spec]
        pn = PhaseNoise(frequency, dbc)
        # TAS technical note is rms = 1.63 deg.
        assert 1.64 < pn.calc_rms_deg(fstart=10, fstop=10**7) < 1.65

        pn_zero = PhaseNoise([], [])
        assert pn_zero.calc_rms_deg() == 0

    def test_calc_rms_deg_data(self):
        freq = []
        dbc_sp = []
        dbc = []
        dbc_spec = []
        fixture_path = 'd:/proj/pyprojects/pl_model/payload/test/__fixtures__/'
        with open(os.path.join(fixture_path, 'phase_noise_s_ka.txt'), 'r') as f:
            for line in f.readlines():
                col_freq, col_pn_sp, col_pn, _, col_spec = [float(x.strip()) for x in line.split('\t')]
                freq.append(col_freq)
                dbc.append(col_pn)
                dbc_sp.append(col_pn_sp)
                dbc_spec.append(col_spec)
        pn = PhaseNoise(freq, dbc)
        pn_sp = PhaseNoise(freq, dbc_sp)
        pn_spec = PhaseNoise(freq, dbc_spec)
        print('\n')
        print('pn with spur = ', pn_sp.calc_rms_deg(), end='\n')
        print('pn without spur = ', pn.calc_rms_deg(), end='\n')
        print('pn_spec = ', pn_spec.calc_rms_deg())
