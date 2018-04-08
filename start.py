#!/usr/bin/python3
#coding: utf8

##Generować dane z błędami!!

#import email
import getopt
#from string import *
from sys import argv

from finanse import iban, kartaKredytowa
from firmowe import firma, regon, nip
from homosapiens import ludek, dataUrodzenia, plec, pesel, dowod, paszport, email, login, haslo
from qth import adresik, telefonkom

__author__="Mariusz 'terminus' Kocoń"
__date__ ="$2013-05-19 11:38:41$"
__info__ ="Generowanie danych do testów, masowe generowanie."

info = '''Wywołanie skryptu wymaga parametrów:
-r lub --id - na początku każdego wiersza zostanie dodany numer, jako np. id do zasilenia nowej tablicy bazy danych.\n
-o nazwa lub -wynik=nazwa - Wyjściowy plik, np: o=plik_z_danymi_wyjsciowymi.csv, jeśli nie podano wyjście na stdout, najczęściej ekran.\n
-i numer lub ilosc=numer - Ilość rekordów wynikowych, np: ilosc=53 wygeneruje 53 rekordy, jeśli brak będzie 1.\n
-b separator lub baza=separator - paramet opcjonalny - w przypadku jego braku zostanie użyty ";".\n
-d lista lub dane=lista_wyników - struktura rekordu wynikowego, dzielone przecinkiem, jeśli brak skrypt zakończy działanie.
    nazwisko - nazwisko i imię
    imie - imię i nazwisko
    wiek=od-do - data urodzenia dla osób w podanym zakresie lat życia, np. wiek*16-67 da ludzi w wieku 16 do 67 lat, czyli w wieku produkcyjnym.
        Jeśli nie podano parametru wieku (liczb po *) przyjęte zostanie 16-67.
    pesel - PESEL do daty urodzenia, wymaga imienia i nazwiska ze względu na sumę kontrolną.
    telefonkom - numer telefonu komórkowego.
    dowod - numer dowodu osobistego.
    paszport - numer paszportu.
    adres=11111 - genruje adres, parametry to 0 lub 1, kolejne pozycje oznaczają:
        1 - generowanie podstaw: kod pocztowy, miejscowość, ulica i numer domu, czasem mieszkania.
            10000: 40-622;Katowice;Jaśminowa 442 m 25
        2 - czy pokazywać gminę.
            11000: 40-622;Katowice;Jaśminowa 442 m 25;Katowice
        3 - czy pokazywać powiat.
            11100: 40-622;Katowice;Jaśminowa 442 m 25;Katowice;Katowice
        4 - czy pokazywać województwo.
            11110: 40-622;Katowice;Jaśminowa 442 m 25;Katowice;Katowice;śląskie;
        5 - czy pokazywać prefixy nazw: gmina, powiat, województwo.
            11111: 40-622;Katowice;Jaśminowa 442 m 25;gmina Katowice;powiat Katowice;woj. śląskie;
    login - login, np do programu, musi być użyty razem z imieniem i nazwiskiem.
    haslo - hasło z losowych znaków.
    e-mail - z losową domeną, musi być użyty razem z imieniem i nazwiskiem.\n
    nrb - numer konta bankowego polskiego banku, UWAGA: lista jednostek bankowych na dzień 2013-06-02,
        zgodna z rejesterm NBP (czyli faktycznie nie wymyślone).
    karta - numer karty kredytowej, jeśli zostanie dodane =wystawca, gdzie wystawca to Maestro, MasterCard, Visa, VisaElectron to wygeneruje TYLKO karty tego wystawcy.\n
    firma - nazwa przedsiębiorstwa z głupia frant, z listy nazwisk i dodania tekstu z kosmosu.
    nip - numer nim, powiązany z przypadkowym US z listy Ministerstwa Finansów, ale nie z urzędem skarbowym podatnika (no chyba że przez przypadek).
    regon - numer REjestru GOspodarki Narodowej, używać tylko dla firm.
\n
Przykładowe polecenie generujące ludzi, w kolejności jak w zapisie separowane średnikiem, 57 rekordów do pliku wychodne.csv:
*   PRZYKŁAD    -> \nstart.py -d imie,wiek=20-67,pesel,dowod,paszport,adres=11111,nrb,e-mail,login,haslo -b ; -i 57 -o wychodne.csv

UWAGA!!
1. Jeśli używasz jako separatora znaku zastrzeżonego w Twoim shellu to poprzedź go bakslashem (\), np w linuxie separator z przykładu powinien wyglądać: -b \;.
2. Zwróć uwagę aby w liście parametrów dla opcji -d nie było spacji.

Najprostrze użycie: skopiuj linijkę powyżej do linii poleceń i usuń co zbędne lub zmień co ma być inne.
Wymagany jest tylko parametr -d (--dane), w przypadku braku pozostałych zostaną użyte parametry domyślne.
'''

#Wystartowanie domyślnych zmiennych
ilosc = 1
separator = ';'
wyjscie = ''
struktura = 0
id = False

try:
    options, args = getopt.getopt(argv[1:], ":hb:d:i:o:r", ["baza=", "ilosc=", "dane=", "wynik=", "help", "id"])
except getopt.GetoptError as skucha:
    print(info)
    print('*********************************************************************************')
    print(str(skucha))
    print('*********************************************************************************')
    exit(1)

#print(options)

if len(options) < 1:
    print(info)
    exit(1)

for u, o in options:
    if u in ('-h', '--help'):
        print(info)
        exit(1)
    elif u in ('-r','--id'):
        id = True
    elif u in ('-d', '--dane'):
        rekord = o.split(',')
        struktura = 1
        #print(rekord)
    elif u in ('-i', '--ilosc'):
        ilosc = int(o)
    elif u in ('-b', '--baza'):
        separator = o
    elif u in ('-o', '--wynik'):
        wyjscie = o
    else:
        print('Nie rozpoznana opcja, proszę wydawać polecenia w sposób zrozumiały.\n Opcja -h pomoże.')

if not struktura:
    print(info)
    print('*********************************************************************************')
    print('Skrypt wymaga podania struktury danych do generowania.')
    print('*********************************************************************************')
    exit(1)

if separator == "tab":
    separator = '\t'

if len(wyjscie) > 1:
    plikWychodny = open(wyjscie, 'w')
    #plikWychodny.write(ustawienia['dane'].replace(',',';') + '\n')

#Wyrzut danych w zadanej ilości
for l in range(ilosc):
    daneWyjsciowe = []
    plec = ''
    
    if id:
        daneWyjsciowe.append(str(l+1))

    #Pętla dająca kolejność z linii poleceń
    for zmienna in rekord:
        zmienna = zmienna.lower()

        #Zawołanie człowieka
        plec = ''
        if zmienna == 'nazwisko':
            p = ludek('n')
            plec = p[1]
            pn = p[0]
            daneWyjsciowe.append(p[0])
        if zmienna == 'imie':
            p = ludek('i')
            plec = p[1]
            daneWyjsciowe.append(p[0])
            pn = p[0]

        #Data urodzenia
        du = ''
        if zmienna.startswith('wiek'):
            p = zmienna.split('=')
            if len(p) == 1:
                p.append('16-67')
            p = p[-1].split('-')
            du = dataUrodzenia(int(p[0]),int(p[1]))
            daneWyjsciowe.append(du)

        #Dowód osobisty
        if zmienna == 'dowod':
            daneWyjsciowe.append(dowod())

        #Paszport
        if zmienna == 'paszport':
            daneWyjsciowe.append(paszport())

        #PESEL
        if zmienna == 'pesel':
            if len(du) < 8:
                du = dataUrodzenia(16,70)
            daneWyjsciowe.append(pesel(du,plec))

        #Adres
        if zmienna.startswith('adres'):
            p = zmienna.split('=')
            p = p[-1]
            while len(p) < 5:
                p = p + '0'
            if not '1' in p:
                p = '10011'
            daneWyjsciowe.append(separator.join(adresik(int(p[0]),int(p[1]),int(p[2]),int(p[3]),int(p[4]))))

        #Numer telefonu komórkowego
        if zmienna == 'telefonkom':
            daneWyjsciowe.append(telefonkom())

        #e-mail
        if zmienna == 'email' or zmienna == 'mail' or zmienna == 'e-mail' or zmienna == 'emil':
            try:
                daneWyjsciowe.append(email(pn))
            except:
                print('Adres e-mail można generować tylko z nazwisk.')

        #login
        if zmienna == 'login':
            try:
                daneWyjsciowe.append(login(pn))
            except:
                print('Login można generować tylko z nazwisk.')

        #hasło
        if zmienna.startswith('haslo'):
            has = zmienna.split('=')
            if has[-1].isdigit():
                has = int(has[-1])
            else:
                has = 8
            daneWyjsciowe.append(haslo(has))

        if zmienna == 'nrb':
            daneWyjsciowe.append(iban('PL'))

        if zmienna.startswith('karta'):
            wystawca = zmienna.split('=')
            if len(wystawca) == 1:
                wystawca = ''
            else:
                wystawca = wystawca[-1]
            daneWyjsciowe.append(kartaKredytowa(wystawca))

        #Firmowe
        if zmienna == 'firma':
            daneWyjsciowe.append(firma())

        if zmienna == 'regon':
            daneWyjsciowe.append(regon())

        if zmienna == 'nip':
            daneWyjsciowe.append(nip())

    if len(wyjscie) > 1:
        plikWychodny.write(separator.join(daneWyjsciowe) + '\n')
    else:
        print(separator.join(daneWyjsciowe))

if len(wyjscie) > 1:
    plikWychodny.close()
