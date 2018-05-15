import os
from ..pahse_noise import PhaseNoise, ChainPhaseNoise


class TestCasePhaseNoise:

    def test_calc_rms_deg(self):
        frequency = [10**x for x in range(1, 8)]
        phase_noise_spec = [-38, -66, -78, -87, -93, -95, -115]
        dbc = [x-6 for x in phase_noise_spec]
        pn = PhaseNoise(frequency, dbc)
        # TAS technical note is rms = 1.63 deg.
        assert 1.64 < pn.calc_rms_deg() < 1.65
        limit_integration = [1000, 10 ** 7]
        assert 1.08 < pn.calc_rms_deg(limit=limit_integration) < 1.1
        pn_zero = PhaseNoise([], [])
        assert pn_zero.calc_rms_deg() == 0

    def test_calc_rms_deg_data(self):
        freq, dbc, dbc_spec = [], [], []
        fixture_path = 'd:/proj/pyprojects/pl_model/payload/test/__fixtures__/'
        with open(os.path.join(fixture_path, 'phase_noise_s_ka.txt'), 'r') as f:
            for line in f.readlines():
                col_freq, _, col_pn, _, col_spec = map(float, line.split('\t'))
                freq.append(col_freq)
                dbc.append(col_pn)
                dbc_spec.append(col_spec)
        pn = PhaseNoise(freq, dbc)
        pn_spec = PhaseNoise(freq, dbc_spec)
        assert 0.5 < pn.calc_rms_deg() < 0.51
        assert 1.63 < pn_spec.calc_rms_deg() < 1.64


class TestCaseChainPhaseNoise:

    def test_calc_chain_phase_noise(self):
        frequency1 = [10 ** x for x in range(1, 8)]
        phase_noise_spec1 = [-38, -66, -78, -87, -93, -95, -115]
        dbc1 = [x - 6 for x in phase_noise_spec1]
        frequency2 = [10 ** x for x in range(1, 8)]
        phase_noise_spec2 = [-38, -66, -78, -87, -93, -95, -115]
        dbc2 = [x - 6 for x in phase_noise_spec2]
        pn1 = PhaseNoise(frequency1, dbc1)
        pn2 = PhaseNoise(frequency2, dbc2)

        ch_pn = ChainPhaseNoise()
        ch_pn.append(pn1)
        ch_pn.append(pn2)
        assert 2.32 < ch_pn.calc_chain_rms_deg() < 2.34
