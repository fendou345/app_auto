# -*- coding: utf-8 -*-
__author__ = 'liuxuexue'

import random, string

class GenerateRandom():
    def string_random(n, ascii = False):
        if ascii == True:
            num = string.ascii_letters + string.digits
        else:
            num = string.digits
        str = "".join(random.sample(num, n))
        return str
