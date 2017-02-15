#!/usr/bin/python3
#coding: utf8
#Moduł generujący dane adresowe
from random import randint
#from string import *

__author__="Mariusz  'terminus' Kocoń"
__date__ ="$2013-05-26 11:39:44$"


#Import miast
adresy=[]
gminy=[]
powiaty=[]
wojewodztwa=[]
f=open("dane/adresy.csv",'r')
for linia in f:
    adresy.append(linia)
    gmina=linia.split(';')[-3]
    if not gmina in gminy:
        gminy.append(gmina)
    powiat=linia.split(';')[-2]
    if not powiat in powiaty:
        powiaty.append(powiat)
    wojewodztwo=linia.split(';')[-1]
    if not wojewodztwo[:-1] in wojewodztwa:
        wojewodztwa.append(wojewodztwo[:-1])
f.close()

def adresik(adr,gmi,pot,woj,pfx):
    """
    Łyka i generuje adres.
    """
    adresout = []
    pf = ''
    adres = adresy[randint(0,len(adresy) - 1)][:-1]
    adres = adres.split(';')
    adres[2] = adres[2] + ' ' + str(randint(1,999))
    if randint(0,1) == 1:
        adres[2] = adres[2] + ' m ' + str(randint(1,99))
    if adr:
        adresout.append(adres[0])
        adresout.append(adres[1])
        adresout.append(adres[2].strip())
    if gmi:
        if pfx:
            pf = 'gmina '
        adresout.append(pf + adres[-4])
    if pot:
        if pfx:
            pf = 'powiat '
        adresout.append(pf + adres[-3])
    if woj:
        if pfx:
            pf = 'woj. '
        adresout.append(pf + adres[-2])
    if len(adresout) == 0:
        adresout.append("Nie podano konfiguracji do generowania adresu!")
    #print(adresout)
    return adresout

def telefonkom():
    """
    Generuje numer telefonu komórkowego
    """
    telefon = "+48"+str(randint(600,799))+str(randint(0,999)).zfill(3)+str(randint(0,999)).zfill(3)
    return telefon
