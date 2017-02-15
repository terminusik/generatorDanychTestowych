# testDataGenerator
Generating data for testing characteristic of Polish and not only (account numbers, credit cards should be as universal), but only for Polish banks.

There is a lack of generating incorrect data, although eg. The control algorithm NIP is a ...feature ;-) ... causing that pass each NIP consisting of one and the same numbers (eg. 000-000-00-00).

Scripts written in Python, should act on both python2 as python3, better will be 3 because of the better service utf.

# generatorDanychTestowych
Generowanie danych do testów charakterystycznych dla Polski i nie tylko (numery kont, kart kredytowych powinny być w miarę uniwersalne), ale tylko dla Polskich banków.

Brakuje generowania danych błędnych, choć w np. algorytmie kontronym NIP jest ... feature ;-) ... pozwodujący że przejdzie każdy NIP złożony z jednej i tej samej cyfry (np. 000-000-00-00).

Skrypty napisane w Pythonie, działać powinny zarówno na Pythonie2 jak na Pythonie3, lepszy będzie 3 ze względu na lepszą obsługę utfa.

Uruchomienie skryptem start.py z parametrami:
Wywołanie skryptu wymaga parametrów:
-o nazwa lub -wynik=nazwa - Wyjściowy plik, np: o=plik_z_danymi_wyjsciowymi.csv, jeśli nie podano wyjście na stdout, najczęściej ekran.

-i numer lub ilosc=numer - Ilość rekordów wynikowych, np: ilosc=53 wygeneruje 53 rekordy, jeśli brak będzie 1.

-b separator lub baza=separator - paramet opcjonalny - w przypadku jego braku zostanie użyty ";".

-d lista lub dane=lista_wyników - struktura rekordu wynikowego, dzielone przecinkiem, jeśli brak skrypt zakończy działanie.
    
    nazwisko - nazwisko i imię
    
    imie - imię i nazwisko
    
    wiek=od-do - data urodzenia dla osób w podanym zakresie lat życia, np. wiek*16-67 ludzi w wieku 16 do 67 lat.
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
  
    e-mail - z losową domeną, musi być użyty razem z imieniem i nazwiskiem.

    nrb - numer konta bankowego polskiego banku, UWAGA: lista jednostek bankowych na dzień 2013-06-02,
        zgodna z rejesterm NBP (czyli faktycznie nie wymyślone).
    karta - numer karty kredytowej, jeśli zostanie dodane =wystawca, gdzie wystawca to Maestro, MasterCard, Visa, VisaElectron to wygeneruje TYLKO karty tego wystawcy.

    firma - nazwa przedsiębiorstwa z głupia frant, z listy nazwisk i dodania tekstu z kosmosu.
    nip - numer nim, powiązany z przypadkowym US z listy Ministerstwa Finansów, ale nie z urzędem skarbowym podatnika (no chyba że przez przypadek).
    regon - numer REjestru GOspodarki Narodowej, używać tylko dla firm.


Przykładowe polecenie generujące ludzi, w kolejności jak w zapisie separowane średnikiem, 57 rekordów do pliku wychodne.csv:
*   PRZYKŁAD    -> 
start.py -d imie,wiek=20-67,pesel,dowod,paszport,adres=11111,nrb,e-mail,login,haslo -b ; -i 57 -o wychodne.csv

UWAGA!!
1. Jeśli używasz jako separatora znaku zastrzeżonego w Twoim shellu to poprzedź go bakslashem (\), np w linuxie separator z przykładu powinien wyglądać: -b \;.
2. Zwróć uwagę aby w liście parametrów dla opcji -d nie było spacji.

Najprostrze użycie: skopiuj linijkę powyżej do linii poleceń i usuń co zbędne lub zmień co ma być inne.
Wymagany jest tylko parametr -d (--dane), w przypadku braku pozostałych zostaną użyte parametry domyślne.
