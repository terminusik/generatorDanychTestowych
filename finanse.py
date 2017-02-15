#!/usr/bin/python3
#coding: utf8

#Dane o finansach: numery kont, karty kredytowe
from random import choice
from random import randint
from string import ascii_uppercase

__author__="Mariusz  'terminus' Kocoń"
__date__ ="$2013-06-02 14:43:40$"

f = open("dane/banki.csv",'r')
banki = []
for linia in f:
    banki.append(linia[:-1])
f.close()

wystawcyKart = {}
wystawcyKart['maestro'] = '5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763, 0604'
wystawcyKart['mastercard'] = '51, 52, 53, 54, 55'
wystawcyKart['visa'] = '4'
wystawcyKart['visaelectron'] = '4026, 417500, 4405, 4508, 4844, 4913, 4917'

dlugoscKart = {}
dlugoscKart['maestro'] = '12, 13, 14, 15, 16, 17, 18, 19'
dlugoscKart['mastercard'] = '16'
dlugoscKart['visa'] = '13,16'
dlugoscKart['visaelectron'] = '16'


def kartaKredytowa(rodzaj):
    '''
    Generowanie numeru karty kredytowe, może być zadany wystawca. Stałą długość 16 znaków, narazie.
    '''
    karta = []
    if len(rodzaj) == 0:
        for i in wystawcyKart.keys():
            karta.append(i)
        karta = choice(karta)
        karta = wystawcyKart[karta].split(',')
        karta = choice(karta).strip()
    else:
        karta = wystawcyKart[rodzaj].split(',')
        karta = choice(karta).strip()
    dlkarty = 16
    while len(karta) < dlkarty - 1:
        karta = karta + str(randint(0,9))
    karta = karta + '0'
    #print(karta)
    karta = karta.zfill(dlkarty)
    sumakt = 0
    for c in range(len(karta) - 1):
        if int(float(c)/2) == float(c)/2:
            kt = int(karta[c]) * 2
            if kt > 9:
                kt = kt - 9
            sumakt = sumakt + kt
        else:
            sumakt = sumakt + int(karta[c])
    sumakt = 10 - sumakt%10
    if sumakt == 10:
        sumakt = 0
    karta = karta[:-1] + str(sumakt)
    return karta

def iban(kraj):
    '''
    Numer Rachunku Bankowego, w standardzie IBAN.
    '''
    #Tablica liter
    litery = {}
    for l in ascii_uppercase:
        litery[l] = ascii_uppercase.index(l) + 10
    krajKod = str(litery[kraj[0]]) + str(litery[kraj[1]])
    bank = banki[randint(0,len(banki) - 1)]
    konto = bank.split(';')[0][:4] + ' ' + bank.split(';')[0][4:]
    while len(konto) < 29:
        num = randint(0,9999)
        num = str(num)
        num = num.zfill(4)
        konto = konto + ' ' + num
    nkonto = int(konto.replace(' ','') + krajKod + '00')
    nkonto = 98 - nkonto%97
    nkonto = str(nkonto).zfill(2)
    konto = kraj + nkonto + ' ' + konto
    return konto
