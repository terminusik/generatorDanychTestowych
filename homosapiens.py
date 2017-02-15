#!/usr/bin/python3
#coding: utf8
#Moduł generujący dane humanoidalne ;-)

#numer paszportu, numer prawa jazdy, tablice samochodowe
#from datetime import date
from random import choice
#from random import randint
from string import ascii_letters
from string import ascii_uppercase
from string import digits

from ogolne import *

__author__="Mariusz  'terminus' Kocoń"
__date__ ="$2013-05-26 15:01:25$"


#Import nazwisk
nazwiska=[]
f=open("dane/nazwiska.csv",'r')
for linia in f:
    nazwiska.append(linia[:-1])
f.close()
nazwiska.sort()

#Import imion
imiona=[]
f=open("dane/imiona.csv",'r')
for linia in f:
    imiona.append(linia[:-1])
f.close()
imiona.sort()

#Tablica liter do dowodu i paszportu
litery = {}
for l in ascii_uppercase:
    litery[l] = ascii_uppercase.index(l) + 10
polskieLiterki = {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s','ż':'z', 'ź':'z'}


def ludek(kolejnosc):
    """
    Generuje imię i nazwisko, parametr to i lub n
    """
    imie = imiona[randint(0,len(imiona)) - 1]
    nazwisko = nazwiska[randint(0,len(nazwiska)) - 1]

    #Odmiana części nazwisko na żeńskie
    if nazwisko[-1] == "i" and plec(imie) == "k":
        nazwisko = nazwisko[:-1] + "a"

    if kolejnosc == "i":
        ludek = imie + " " + nazwisko
    else:
        ludek = nazwisko + " " + imie
    ludek = [ludek, plec(imie)]
    return ludek

def dataUrodzenia(od,do):
    """
    Generuje losową datę urodzenia w podanym zakresie wieku
    """
    rok = date.today().year
    rokod = rok - od
    rokdo = rok - do
    data = dataLosowana(rokod, rokdo)
    return str(data)

def plec(imie):
    """
    Płeć na podstawie imienia
    """
    if imie[-1] == "a":
        plec = "k"
    else:
        plec = "m"
    return plec

def pesel(dataUrodzenia, plec):
    """
    Genruje PESEL
    """
    wyrozniki=("1800:1899:80","1900:1999:0","2000:2099:20","2100:2199:40","2200:2299:60")
    wagi=(1,3,7,9,1,3,7,9,1,3)
    rok = int(dataUrodzenia.split("-")[0])
    miesiac = int(dataUrodzenia.split("-")[1])

    #Wyróżnik wieku kalendarzowego
    for i in wyrozniki:
        wyr=i.split(":")
        if rok >= int(wyr[0]) and rok <= int(wyr[1]):
            miesiac = miesiac + int(wyr[2])
    miesiacs = str(miesiac).zfill(2)

    #Porządkowy losowo
    porzadkowy = randint(1,9998)
    #Płeć, da kobiet parzysty dla mężczyzn nieparzysty
    if plec == "k" and float(porzadkowy)/2 != int(float(porzadkowy)/2):
        porzadkowy = porzadkowy + 1
    elif plec == "m" and float(porzadkowy)/2 == int(float(porzadkowy)/2):
        porzadkowy = porzadkowy + 1
    porzadkowys = str(porzadkowy).zfill(4)

    #Suma kontrolna
    pesel = str(rok)[2:] + miesiacs + dataUrodzenia.split("-")[-1] + porzadkowys
    sk = 0
    for i in range(10):
        iloczyn = int(pesel[i])*wagi[i]
        sk = sk + iloczyn
    sk = sk%10
    sk = 10 - sk
    sk  = sk%10

    pesel = str(rok)[2:] + miesiacs + dataUrodzenia.split("-")[-1] + porzadkowys + str(sk)
    return pesel

def dowod():
    '''
    Generuje losowy numer dowodu osobistego PL
    '''
    wagi = (7,3,1,7,3,1,7,3)
    seria = ''
    while len(seria) < 3:
        seria = seria + choice(ascii_uppercase)
    numer = str(randint(1,99999)).zfill(5)
    sumkt = 0
    dowod = seria + numer
    for i in range(8):
        if dowod[i].isalpha():
            sumkt = sumkt + (litery[dowod[i]] + 10) * wagi[i]
        elif dowod[i].isdigit():
            sumkt = sumkt + int(dowod[i]) * wagi[i]
    sumkt = sumkt%10
    dowod = seria + str(sumkt) + str(numer)
    return dowod

def paszport():
    '''
    Generuje losowy numer paszportu PL
    '''
    wagi = (7,3,9,1,7,3,1,7,3)
    seria = ''
    while len(seria) < 2:
        seria = seria + choice(ascii_uppercase)
    numer = str(randint(1,999999)).zfill(6)
    sumkt = 0
    paszport = seria + numer
    for i in range(8):
        if paszport[i].isalpha():
            sumkt = sumkt + (litery[paszport[i]] + 10) * wagi[i]
        elif paszport[i].isdigit():
            sumkt = sumkt + int(paszport[i]) * wagi[i]
    sumkt = sumkt%10
    paszport = seria + str(sumkt) + str(numer)
    return paszport

def email(inazwisko):
    '''
    Tworzy e-mail z losową domeną, z imienia i nazwiska
    '''
    domeny = ['gmail.com','onet.pl','poczta.pl','e-mail.pl','listonosz.pl']
    mailuser = login(inazwisko)
    email = mailuser + '@' + domeny[randint(0, len(domeny) - 1) ]
    return email

def login(inazwisko):
    '''
    Tworzy login z podanego imienia i nazwiska
    '''
    login = inazwisko.split(' ')
    login = (login[0][:1] + login[-1]).lower()
    for znak in login:
        if znak in polskieLiterki:
            login = login.replace(znak, polskieLiterki[znak])
    return login

def haslo(dl):
    '''
    Hasło z losowych znaków o zadanej długości.
    '''
    haslo = ''
    while len(haslo) < dl:
        haslo = haslo + choice(ascii_letters+digits+' ,.<>?/|[]()-=+_@#$%^&*!')
    return haslo
