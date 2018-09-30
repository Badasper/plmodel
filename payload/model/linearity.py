class Linearity:
    """
    Convert IP3 <-> OIP3 <-> G,P,IM3
    """

    def __init__(self, *, oip, gain):
        self._oip = oip
        self._gain = gain

    @classmethod
    def iip(cls, *, iip, gain):
        oip = iip + gain
        return cls(oip=oip, gain=gain)

    @classmethod
    def intermod(cls, *, input_power, gain, intermod_level):
        oip = intermod_level / 2 + input_power + gain
        return cls(oip=oip, gain=gain)

    def get_dbc(self, input_power=0):
        output_power = input_power + self._gain
        return (self._oip - output_power) * 2

    def get_oip(self):
        return self._oip

    def get_iip(self):
        return self._oip - self._gain
