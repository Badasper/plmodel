# -*- coding: utf-8 -*-
"""
Created on 
@author: Yakovlev Alexander
"""

from payload.model.receive_channel import ReceiveRFChannel


def format_data(elem):
    data = elem['start'], elem['stop'], elem['center'], elem['nLO'], elem['mRF']
    formatting_str = '{:>8.2f} -- {:>8.2f} :: fc = {:8.2f}  nLO={:>3}, mLO={:>3}'
    return formatting_str.format(*data)


def pretty_receive_channels(channel, lower, upper):
    comb = channel.get_all_combinations()
    comb = filter(lambda x: lower < x['start'] < upper, comb)

    print('\nCombination channels:\n')
    for item in comb:
        print(format_data(item))
    print('\nMain channel:')
    item = channel.main_receive(convert='down')
    print(format_data(item))
    print('\nImage channel:')
    item = channel.image_receive(convert='down')
    print(format_data(item))


speed_link = {'receive': 0,
              'transmit': 20000}

inter_sat_link_k = {'receive': 37000,
                    'transmit': 30000}

inter_sat_link_s = {'receive': 2300,
                    'transmit': 2100}

test_link = {'receive': 30000,
             'transmit': 37000}

inter_sat_ch = {
    'intermediate_frequency': inter_sat_link_k['transmit'],
    'bandwidth_channel': 2,
    'local_oscillator_frequency': 7000
}
inter_sat_ch = ReceiveRFChannel(**inter_sat_ch)
pretty_receive_channels(inter_sat_ch, 20000, 60000)

print(inter_sat_ch.get_lo_harmonics())