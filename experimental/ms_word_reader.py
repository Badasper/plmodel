# -*- coding: utf-8 -*-
"""
Created on 
@author: Yakovlev Alexander
"""

import re
import codecs

with open('abbr.txt', 'r', encoding='utf-8') as f:
    data = f.readline()

pattern = r'\b(?:[А-Я]*){2,5}(?=\s|$)'

answer = re.findall(pattern, data)
print(answer)
# answer.sort()
# for item in answer:
#     print(item)
#
# print(len(answer))