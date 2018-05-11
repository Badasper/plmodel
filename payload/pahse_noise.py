from .rfutil import calc_rms_rad,\
                         calc_interp_rms_rad,\
                         convert_rad_to_deg


class PhaseNoise:

    def __init__(self, frequency, dbc):
        self._frequency = frequency
        self._dbc = dbc

    def calc_rms_rad(self, fstart=None, fstop=None, points=None):
        if points is None:
            points = 1000
        if len(self._frequency) > points:
            return calc_rms_rad(self._frequency, self._dbc, fstart=fstart, fstop=fstop)
        return calc_interp_rms_rad(self._frequency, self._dbc, points)

    def calc_rms_deg(self, fstart=None, fstop=None, points=None):
        rms_rad = self.calc_rms_rad(fstart=fstart, fstop=fstop, points=points)
        return convert_rad_to_deg(rms_rad)
