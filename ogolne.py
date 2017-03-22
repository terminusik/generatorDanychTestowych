#!/usr/bin/python3
#coding: utf8
#Biblioteka funkcje nieprzyporządkowanych

from datetime import date, datetime
from random import randint, uniform

__author__="Mariusz  'terminus' Kocoń"
__date__ ="$2013-05-31 21:37:54$"

def dataLosowana(od,do):
    roki = [od, do]
    roki.sort()
    return date.fromtimestamp(uniform(datetime(roki[0], 1, 1, 0, 0, 0).timestamp(), datetime(roki[1], 12, 31, 23, 59, 59).timestamp()))
