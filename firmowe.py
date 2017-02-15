#!/usr/bin/python3
#coding: utf8
from random import choice
from random import randint

#Dane firm, nazwa, nip, regon

__author__="Mariusz  'terminus' Kocoń"
__date__ ="$2013-06-02 14:47:30$"

wlasnosc = (" Przedsiębiorstwo Państwowe", " Spółka Akcyjna", " Spółka z O.O.", " i spółka", " firma rodzinna", " i synowie")
nastki = ("POL", "X", "")

us = []
f = open("dane/kodyUrzedowSkarbowych.csv",'r')
for linia in f:
    us.append(linia[:-1])
f.close()

#Import nazwisk - zrobimy z nich nazwy firm
nazwiska=[]
f=open("dane/nazwiska.csv",'r')
for linia in f:
    nazwiska.append(linia[:-1])
f.close()


def firma():
    '''
    Nazwa firmy generowana z losowego nazwiska.
    '''
    firmaout = choice(nazwiska).strip() + choice(wlasnosc)
    return firmaout


def nip():
    '''
    Numer NIP, wystawiony ;-) przez istniejący US, ale nie koniecznie zgodny z miejscem prowadzonej "działalności"
    '''
    uskod = choice(us).split(';')[0].strip()
    wagi = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    sumkt = 10
    while sumkt == 10:
        sumkt = 0
        nipout = uskod
        while len(nipout) < 9:
            nipout = nipout + str(randint(0,9))
        for i in range(9):
            sumkt = sumkt + int(nipout[i]) * wagi[i]
        sumkt = sumkt%11
    return nipout + str(sumkt)

def regon():
    '''
    REGON zgodny z zasadami 9 dla siedzib centralnych 14 dla oddziałów firm.
    '''
    dlugosc = choice([9, 14])
    if dlugosc == 9:
        regonout = regonik('')
    else:
        regonout = regonik('')
        regonout = regonik(regonout)
    return regonout

def regonik(wstep):
    '''
    Wyliczenie cyfr kontrolnych dla funkcji REGON, wydzielone bo regony 14 znakowe mają liczoną dla 9 i dla 14
    '''
    if len(wstep) == 0:
        dlugosc = 9
    else:
        dlugosc = 14
    wagi9 = (8, 9, 2, 3, 4, 5, 6, 7)
    wagi14 = (2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8)
    sumkt = 0
    if dlugosc == 9:
        wagi = wagi9
    else:
        wagi = wagi14
    regonout = wstep
    while len(regonout) < dlugosc - 1:
        regonout = regonout + str(randint(0,9))
    for i in range(dlugosc - 1):
        sumkt = sumkt + int(regonout[i]) * wagi[i]
    sumkt = sumkt%11
    if sumkt == 10:
        sumkt = 0
    return regonout + str(sumkt)
