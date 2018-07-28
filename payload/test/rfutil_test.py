# -*- coding: utf-8 -*-
"""
Created on 17/05/18
@author: Yakovlev Alexander
"""

from payload.rf_calc import rfutil as rf


class TestCaseBaseTools:
    def test_base_tools(self):
        assert rf.hz_to_m(5 * 10**9) == 0.06
        assert rf.m_to_hz(0.06) == 5 * 10**9


class TestCaseLogTools:
    def test_log_tools(self):
        assert rf.from_db(10) == 10
        assert rf.to_db(10) == 10
        assert rf.dbm_to_dbw(10) == -20
        assert rf.dbw_to_dbm(5) == 35
        assert rf.dbm_to_watt(30) == 1.0
        assert rf.dbw_to_watt(10) == 10.0
        assert rf.watt_to_dbm(10) == 40
        assert 3.14 < rf.deg_to_rad(180) < 3.142


class TestCaseRadioLinkTools:
    def test_radiolink_tools(self):
        assert rf.eirp(10, 10) == 20
        assert -154 < rf.pfd(10, 42000000) < -153
        assert -164 < rf.free_space_loss(42000000) < -163
        power_w = 10
        gain_tx = 20
        eirp_tx = rf.eirp(power_w, gain_tx)
        pfd_user = rf.pfd(eirp_tx, 42000000)
        gain_at_frequency = (38.8, 5.725 * 10**9)
        assert -132 < rf.power_rx(pfd_user, gain_at_frequency) < -131
