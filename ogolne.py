#!/usr/bin/python3
#coding: utf8
#Biblioteka funkcje nieprzyporządkowanych

from datetime import date
from random import randint

__author__="Mariusz  'terminus' Kocoń"
__date__ ="$2013-05-31 21:37:54$"

def dataLosowana(od,do):
    roki = [od, do]
    roki.sort()
    rok = randint(roki[0],roki[1])
    miesiac = randint(1,12)
    if miesiac == 2:
        lutymax = 28
        if float(rok)/4 == int(float(rok)/4):
            if float(rok)/100 == int(float(rok)/100):
                if float(rok)/400 == int(float(rok)/400):
                    lutymax = 29
                else:
                    lutymax = 28
            else:
                lutymax = 29
        dzien = randint(1,lutymax)
    elif miesiac in [1,3,5,7,8,10,12]:
        dzien = randint(1,31)
    else:
        dzien = randint(1,30)
    data = date(rok, miesiac, dzien)
    return data