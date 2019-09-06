# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

import re
import csv

def getCsvData(pathname):
    #读取CSV文件
    value_rows = []
    with open(pathname, encoding='UTF-8') as f:
        f_csv = csv.reader(f)
        next(f_csv)
        for r in f_csv:
            value_rows.append(r)
    return value_rows
