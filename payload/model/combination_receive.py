# -*- coding: utf-8 -*-
"""
Скрипт для определения частот побочных каналов конвертера

Yakovlev AY 02.12.16
ver 0.3 modify 18/04/17
ver 1.0 modify 23/07/8

"""

__author__ = "Yakovlev AY"
__version__ = "1.0"


def is_equal_nm(item, key1="nLO", key2="mRF"):
    return abs(item[key1]) == abs(item[key2])


def calc_combination(m=1, n=1, low_frequency=0, upper_frequency=0, bw=0):
    """Расчет комбинации включая отрицательные частоты"""
    start_frequency = low_frequency / m - bw / (2 * m) - upper_frequency * n / m
    stop_frequency = low_frequency / m + bw / (2 * m) - upper_frequency * n / m
    return start_frequency, stop_frequency


class MainImageReceiveCombination:
    def __init__(self, intermediate_frequency, local_oscillator_frequency):
        is_lo_bigger = local_oscillator_frequency > intermediate_frequency
        self._main_image_combinations = {
            "up": {
                "main": {
                    "mRF": 1,
                    "nLO": 1
                },
                "image": {
                    "mRF": 1,
                    "nLO": -1
                }
            },
            "down": {
                "main": {
                    "mRF": 1,
                    "nLO": -1
                },
                "image": {
                    "mRF": -1,
                    "nLO": 1
                } if is_lo_bigger else {
                    "mRF": 1,
                    "nLO": 1
                },
            },
            "inverse": {
                "main": {
                    "mRF": -1,
                    "nLO": 1
                },
                "image": {
                    "mRF": 1,
                    "nLO": -1
                }
            },
        }

    def get_image(self, converter_direction="down"):
        if converter_direction not in self._main_image_combinations:
            raise ValueError("Converter mus be up, down or inverse!")
        return self._main_image_combinations[converter_direction]["image"]

    def get_main(self, converter_direction="down"):
        if converter_direction not in self._main_image_combinations:
            raise ValueError("Converter mus be up, down or inverse!")
        return self._main_image_combinations[converter_direction]["main"]


class ReceiveRFChannel:
    def __init__(self,
                 intermediate_frequency=0,
                 bandwidth_channel=0,
                 local_oscillator_frequency=0,
                 direction=None):
        self._if = intermediate_frequency
        self._bw = bandwidth_channel
        self._lo = local_oscillator_frequency
        self._direction = direction

    @classmethod
    def rx(cls, rx_frequency=0, tx_frequency=0, bandwidth_channel=0):
        local_oscillator_frequency = abs(rx_frequency - tx_frequency)
        direction = 'up' if rx_frequency < tx_frequency else 'down'
        return cls(
            intermediate_frequency=tx_frequency,
            local_oscillator_frequency=local_oscillator_frequency,
            bandwidth_channel=bandwidth_channel,
            direction=direction)

    def _calc_receive_channel(self, mRF=1, nLO=1):
        """Расчет комбинации включая отрицательные частоты"""
        n, m = nLO, mRF
        start_frequency = self._if / m - self._bw / (2 * m) - self._lo * n / m
        stop_frequency = self._if / m + self._bw / (2 * m) - self._lo * n / m
        if start_frequency > stop_frequency:
            start_frequency, stop_frequency = stop_frequency, start_frequency
        receive_channel_data = {
            "start": start_frequency,
            "stop": stop_frequency,
            "center": (stop_frequency - start_frequency) / 2 + start_frequency,
            "nLO": n,
            "mRF": m,
        }
        return receive_channel_data

    def get_all_combinations(self, mRF=10, nLO=10):
        """Побочные каналы приема:
        Все побочные каналы приема,
        Fпкп = IF/m - LO*n/m"""
        mRF_lst = [m for m in range(-mRF, mRF + 1) if m != 0]
        nLO_lst = [n for n in range(-nLO, nLO + 1)]
        combination_lst = [
            self._calc_receive_channel(m, n) for m in mRF_lst for n in nLO_lst
        ]
        filtered_combinations = filter(lambda x: x["stop"] >= 0,
                                       combination_lst)
        sorted_combinations = sorted(
            filtered_combinations, key=lambda x: x["start"])
        return list(sorted_combinations)

    def main_receive(self, convert="down"):
        """Основной канал приема Fпрм = IF/m - LO*n/m, где n=1, m=1"""
        if self._direction:
            convert = self._direction
        combination = MainImageReceiveCombination(self._if,
                                                  self._lo).get_main(convert)
        mRF, nLO = combination["mRF"], combination["nLO"]
        return self._calc_receive_channel(mRF=mRF, nLO=nLO)

    def image_receive(self, convert="down"):
        """Побочный канал приема:
        Зеркальный канал приема,
        Опасен тем, что имеет одинаковый отклик как и основной канал приёма,
        Fз = IF/m - LO*n/m при m, n = (inverse, up:  = (1, -1),
        down: LO > ПЧ = (-1, 1), LO < ПЧ = (1, 1))
        image_receive()"""
        if self._direction:
            convert = self._direction
        combination = MainImageReceiveCombination(self._if,
                                                  self._lo).get_image(convert)
        mRF, nLO = combination["mRF"], combination["nLO"]
        return self._calc_receive_channel(mRF=mRF, nLO=nLO)

    def intermediate_receive(self):
        """Побочный канал приема:
        Канал приема на промежуточной частоте,
        опасен малым подавлением в миксере,
        Fпкп = IF,
        intermediate_receive()"""
        return self._calc_receive_channel(mRF=1, nLO=0)

    def combinations_receive(self, mRF=10, nLO=10):
        """Побочный канал приема:
        Комбинационный канал приема,
        Fпкп = IF/m - LO*n/m
        при остальных m и n
        get_combination_receive(mRF=10, nLO=10)"""
        all_combinations = self.get_all_combinations(mRF=mRF, nLO=nLO)
        exclude_combinations = [
            self.intermediate_receive(),
            self.image_receive(),
            self.main_receive(),
        ]
        combinations_receive = filter(lambda x: x not in exclude_combinations,
                                      all_combinations)
        return list(combinations_receive)

    def equal_nm_receive(self, mRF=10, nLO=10):
        """Побочный канал приема:
        Частный случай комбинационного канала приема,
        опасны близким расположением к основному каналу приёма,
        Fпкп = IF/m -+ LO*n/m,
        при m=n
        equal_nm_receive(mRF=10, nLO=10)"""
        all_combinations = self.get_all_combinations(mRF=mRF, nLO=nLO)
        equal_nm_receive_channels = filter(lambda x: is_equal_nm(x),
                                           all_combinations)
        return list(equal_nm_receive_channels)

    def get_lo_harmonics(self, nLO=10):
        return {"{}HLO".format(n): self._lo * n for n in range(1, nLO + 1)}

    def converter_direction(self):
        return self._direction
