# -*- coding: utf-8 -*-
"""
Скрипт для определения частот побочных каналов конвертера

Yakovlev AY 02.12.16
ver 0.3 modify 18/04/17
ver 1.0 modify 23/07/8

"""

__author__ = "Yakovlev AY"
__version__ = '1.0'


class MainImageReceiveCombination:

    def __init__(self, intermediate_frequency, local_oscillator_frequency):
        is_lo_bigger = local_oscillator_frequency > intermediate_frequency
        self._main_image_combinations = {
            'up': {
                'main': {'mRF': 1, 'nLO': 1},
                'image': {'mRF': 1, 'nLO': -1}
            },
            'down': {
                'main': {'mRF': 1, 'nLO': -1},
                'image': {'mRF': -1, 'nLO': 1} if is_lo_bigger else {'mRF': 1, 'nLO': 1}
            },
            'inverse': {
                'main': {'mRF': -1, 'nLO': 1},
                'image': {'mRF': 1, 'nLO': -1}
            }
        }

    def get_image(self, converter_direction='down'):
        if converter_direction not in self._main_image_combinations:
            raise ValueError('Converter mus be up, down or inverse!')
        return self._main_image_combinations[converter_direction]['image']

    def get_main(self, converter_direction='down'):
        if converter_direction not in self._main_image_combinations:
            raise ValueError('Converter mus be up, down or inverse!')
        return self._main_image_combinations[converter_direction]['main']


class ReceiveRFChannel:

    def __init__(self,
                 intermediate_frequency,
                 bandwidth_channel,
                 local_oscillator_frequency,
                 converter_direction='down'):

        self._if = intermediate_frequency
        self._bw = bandwidth_channel
        self._lo = local_oscillator_frequency
        self._direction = converter_direction

    def _calc_receive_channel(self, mRF=10, nLO=10):
        """Расчет комбинации включая отрицательные частоты"""
        n, m = nLO, mRF
        start_frequency = self._if / m - self._bw / (2 * m) - self._lo * n / m
        stop_frequency = self._if / m + self._bw / (2 * m) - self._lo * n / m
        if start_frequency > stop_frequency:
            start_frequency, stop_frequency = stop_frequency, start_frequency
        receive_channel = {
            'start': start_frequency,
            'stop': stop_frequency,
            'center': (stop_frequency - start_frequency) / 2 + start_frequency,
            'nLO': n,
            'mRF': m
        }
        return receive_channel

    def get_all_combinations(self, mRF=10, nLO=10):
        """Побочные каналы приема:
        Все побочные каналы приема,
        Fпкп = IF/m - LO*n/m"""
        mRF_lst = [m for m in range(-mRF, mRF + 1) if m != 0]
        nLO_lst = [n for n in range(-nLO, nLO + 1)]
        combination_lst = [self._calc_receive_channel(m, n) for m in mRF_lst for n in nLO_lst]
        combinations = filter(lambda x: x['start'] >= 0, combination_lst)
        return list(combinations)

    def main_receive(self):
        """Основной канал приема Fпрм = IF/m - LO*n/m, где n=1, m=1"""
        combination = MainImageReceiveCombination(self._if, self._lo).get_main(self._direction)
        mRF, nLO = combination['mRF'], combination['nLO']
        return self._calc_receive_channel(mRF=mRF, nLO=nLO)

    def image_receive(self):
        """Побочный канал приема:
        Зеркальный канал приема,
        Опасен тем, что имеет одинаковый отклик как и основной канал приёма,
        Fз = IF/m - LO*n/m при m, n = (inverse, up:  = (1, -1), down: LO > ПЧ = (-1, 1), LO < ПЧ = (1, 1))
        image_receive()"""
        combination = MainImageReceiveCombination(self._if, self._lo).get_image(self._direction)
        mRF, nLO = combination['mRF'], combination['nLO']
        return self._calc_receive_channel(mRF=mRF, nLO=nLO)

    def intermediate_receive(self):
        """Побочный канал приема:
        Канал приема на промежуточной частоте,
        опасен малым подавлением в миксере,
        Fпкп = IF,
        intermediate_receive()"""
        return self._calc_receive_channel(mRF=1, nLO=0)

    def subharmonic_receive(self, max_order_m=10):
        """Побочный канал приёма:
        Канал приёма на субгармонике,
        Fпкп = IF/m -+ LO*n/m,
        n=1, m=1...m
        subharmonic_receive(max_order=m)"""
        return [item for item in self.get_all_combinations(max_order_m, 1) if item['start'] >= 0]

    def combinations_receive(self, mRF=10, nLO=10):
        """Побочный канал приема:
        Комбинационный канал приема,
        Fпкп = IF/m - LO*n/m
        при остальных m и n
        get_combination_receive(mRF=10, nLO=10)"""
        all_combinations = self.get_all_combinations(mRF=mRF, nLO=nLO)
        exclude_combinations = []
        exclude_combinations.append(self.intermediate_receive())
        exclude_combinations.append(self.image_receive())
        exclude_combinations.append(self.main_receive())
        for subharmonic in self.subharmonic_receive(max_order_m=mRF):
            exclude_combinations.append(subharmonic)
        combinations_receive = []
        for combination in all_combinations:
            if combination not in exclude_combinations:
                combinations_receive.append(combination)
        return combinations_receive

    def equal_nm_receive(self, mRF=10, nLO=10):
        """Побочный канал приема:
        Частный случай комбинационного канала приема,
        опасны близким расположением к основному каналу приёма,
        Fпкп = IF/m -+ LO*n/m,
        при m=n
        equal_nm_receive(mRF=10, nLO=10)"""
        equal_nm_receive_channels = []
        for item in self.get_all_combinations(mRF=mRF, nLO=nLO):
            if abs(item['nLO']) == abs(item['mRF']):
                equal_nm_receive_channels.append(item)
        return equal_nm_receive_channels
