from payload.experimental.frequency_stability import FrequencyStability


class TestCaseFrequencyStability:

    def stability_test(self):
        fst = FrequencyStability(ppm=2)

        assert fst.get_freq_offset(frequency=5e6) == 100  # Hz
