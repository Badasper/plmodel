# -*- coding: utf-8 -*-
"""
Created on 10/07/18
@author: Yakovlev Alexander
"""


class Equipment:
    def __init__(self, pos_name):
        self._pos_name = pos_name

    def get_pos_name(self):
        return self._pos_name

    def get_data(self, query):
        data = query.get_from_db(self.get_pos_name())
        return data
