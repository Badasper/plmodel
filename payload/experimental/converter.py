# -*- coding: utf-8 -*-
"""
Скрипт для определения частот побочных каналов конвертера

Yakovlev AY 02.12.16
ver 0.3 modify 18/04/17

"""


import codecs

__author__ = "Yakovlev AY"
__version__ = '0.3'


def create_file(lst, namef):
    """
    запись в файл массива

    """
    with codecs.open(namef, 'w', encoding='utf-8') as f:
        for item in lst:
            f.write(item + "\n")
    print('end')


def calc_mixproduct(n, m, center_IF, BW_IF, LO):
    fstart = (center_IF/n - BW_IF/(2*n)) - m/n*(LO)
    fstop = (center_IF/n + BW_IF/(2*n)) - m/n*(LO)
    return [fstart, fstop]


def inband(txband, fstart, fstop):
    for tx_band in txband:
        if tx_band[0] < fstart < tx_band[1] or \
           tx_band[0] < fstop < tx_band[1] or \
           (fstart < tx_band[0] and fstop > tx_band[1]):
            print('Yes')
            return True
    return False


def append_channel(dataOut, txband, *lst_params):
    n = lst_params[0]
    m = lst_params[1]

    # проверка на инверсию спектра
    if n >= 0:
        fstart, fstop = calc_mixproduct(*lst_params)
    else:
        fstop, fstart = calc_mixproduct(*lst_params)
    # проверка на физичность
    if fstop >= 0:
        # проверка передающего диапазона в побочном канале приема

        if inband(txband, fstart, fstop):
            dataOut.append('---- Обратить внимание! ----')
        dataOut.append("n*RF = {0}, "
                       "m*LO = {1}, "
                       "Fstart = {2} МГц, "
                       "Fstop = {3} МГц".
                       format(n, m, round(fstart, 2),
                              round(fstop, 2)))


def receive_channels(center_IF, BW_IF, LO_lst, txband, n=5, m=5):
    """
    расчет частот побочных каналов приема
    """
    nlst = [x for x in range(-n, n+1) if x != 0]
    mlst = [x for x in range(-m, m+1)]

    dataOut = ["нелинейные продукты n*RF = {} x m*LO = {}".format(n, m)]
    for LO in LO_lst:
        dataOut.append('\n')
        dataOut.append("{} LO = {} МГц {}".format("*"*26, LO, "*"*26))
        for n in nlst:
            for m in mlst:
                append_channel(dataOut, txband, n, m, center_IF, BW_IF, LO)
    return dataOut
