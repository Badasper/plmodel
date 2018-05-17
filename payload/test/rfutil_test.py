# -*- coding: utf-8 -*-
"""
Created on 17/05/18
@author: Yakovlev Alexander
"""

from payload import rfutil as rf


class TestCaseLogTools:

    def test_log_tools(self):
        assert rf.from_db(10) == 10
        assert rf.to_db(10) == 10
        assert rf.dbm_to_dbw(10) == -20
        assert rf.dbw_to_dbm(5) == 35
        assert rf.dbm_to_watt(30) == 1.0
        assert rf.dbw_to_watt(10) == 10.0


class TestCaseRadioLinkTools:

    def test_radiolink_tools(self):
        assert rf.eirp(10, 10) == 20
        assert -154 < rf.pfd(10, 42000000) < -153
        assert 164 > rf.free_space_loss(42000000) > 163
        power_w = 5
        gain_tx = 25
        eirp_tx = rf.eirp(power_w, gain_tx)
        pfd_tx = rf.pfd(eirp_tx, 42000000)
        print(pfd_tx)
        gain_vs_wavelength = (38.8, 0.045)
        print(rf.power_rx(pfd_tx, gain_vs_wavelength) + 30)
        assert -91 < rf.power_rx(pfd_tx, gain_vs_wavelength) < -90
