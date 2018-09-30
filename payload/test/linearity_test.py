from payload.model.linearity import Linearity


class TestCaseLinearity:
    def test_oip(self):
        oip = 18
        gain = 20
        ampl = Linearity(oip=oip, gain=gain)
        assert ampl.get_dbc(-20) == 36
        assert ampl.get_iip() == -2
        assert ampl.get_oip() == 18

    def test_iip(self):
        gain = 20
        iip = -2
        ampl = Linearity.iip(iip=iip, gain=gain)
        assert ampl.get_dbc(-20) == 36
        assert ampl.get_iip() == -2
        assert ampl.get_oip() == 18

    def test_intermod(self):
        gain = 20
        intermod = 36
        ampl = Linearity.intermod(
            intermod_level=intermod, gain=gain, input_power=-20)
        assert ampl.get_dbc(-20) == 36
        assert ampl.get_iip() == -2
        assert ampl.get_oip() == 18
