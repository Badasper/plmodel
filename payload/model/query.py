# -*- coding: utf-8 -*-
"""
Created on 11/07/18
@author: Yakovlev Alexander
"""
import os


# TODO query to data base:
def get_data_from_db(param, param2):
    data = {'x': [], 'y': []}
    filepath = os.getcwd() + '/payload/test/__fixtures__/GF_WF1.txt'
    with open(filepath, 'r') as f:
        for line in f.readlines():
            point = line.split()
            data['x'].append(float(point[0]))
            data['y'].append(float(point[1]))
    return data


class Query:
    pass


class QueryData(Query):
    def __init__(self, condition, code_measurement):
        self._condition = condition
        self._code = code_measurement

    def get_from_db(self, pos_name):
        condition = self._condition.get_condition()
        # TODO query to data base
        return get_data_from_db(condition, self._code)
