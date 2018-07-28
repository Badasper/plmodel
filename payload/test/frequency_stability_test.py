from payload.model.frequency_stability import (FrequencyStability,
                                               ChainFrequencyStability)


class TestCaseFrequencyStability:
    def test_frequency_stability(self):
        freq_stability = FrequencyStability(LO=5e9, ppm=2)
        assert freq_stability.calc_offset() == 10000  # Hz

    def test_chain_frequency_offset(self):
        chain_freq_stability = ChainFrequencyStability()
        freq_stability_1 = FrequencyStability(LO=4e9, ppm=1.5)
        freq_stability_2 = FrequencyStability(LO=3e9, ppm=0.8)
        chain_freq_stability.append(freq_stability_1)
        chain_freq_stability.append(freq_stability_2)

        assert 6462.19 < chain_freq_stability.calc_offset() < 6462.2  # Hz

        chain_freq_stability_init = ChainFrequencyStability([
            FrequencyStability(LO=4e9, ppm=1.5),
            FrequencyStability(LO=3e9, ppm=0.8)
        ])
        assert 6462.19 < chain_freq_stability_init.calc_offset() < 6462.2  # Hz

        assert chain_freq_stability_init.calc_offset_worst() == 8400.0  # Hz
