# -*- coding: utf-8 -*-
"""
Created on 11/07/18
@author: Yakovlev Alexander
"""


class Condition:
    def __init__(self, temp, pressure):
        self._temp = temp
        self._pressure = pressure

    def get_condition(self):
        return {"temperature": self._temp, "pressure": self._pressure}
