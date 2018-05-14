# -*- coding: utf-8 -*-
"""
Created on 14/05/18
@author: Yakovlev Alexander
"""
names = []
pos_nums = []

pos_names_flag = False


with open('Sheet1utf8.NET', 'r', encoding='utf8') as f:
    for line in f.readlines():
        if not line.strip():
            continue
        if line.startswith('<<< Wire List >>>'):
            pos_names_flag = False
        if pos_names_flag:
            strp_line = line.strip()
            name, pos_no = [x.strip() for x in strp_line.split(' ') if x]
            names.append(name)
            pos_nums.append(pos_no)
        if line.startswith('<<< Component List >>>'):
            pos_names_flag = True
print(len(names))

name_dict = {
    'Coaxial_cable': "Кабель коаксиальный",
    'Ku/C ': "Конвертер Ku/C-диапазона",
    'L/C ': "Конвертер L/C-диапазона",
    'C/ПЧ': "Конвертер C/ПЧ-диапазона",
    'Divider_4port': "делитель",
    'DTP': "Цифровой мультплексор",
    'Filter': "Фильтр",
    'WR137': "Волновод WR137",
    'Test_coupler': "тестовый ответвитель",
    'Isolator_coaxial': "изолятор коаксиальный",
    'Adaptor_Female/Female': "коаксиальный переход",
    'Load': "нагрузка",
    'LNA': "МШУ",
    'Switch_C-type ': "Переключатель коаксиальный С-типа",
}

from openpyxl import Workbook
wb = Workbook()

ws = wb.active
for item in zip(names, pos_nums):
    ws.append(item)


wb.save('net_list.xlsx')


