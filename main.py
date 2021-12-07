'''
Bejelentkezés

Írjon programot, amely azt vizsgálja, hogy egy felhasználó helyesen adja-e meg a jelszavát! 
A program addig kérdezi újra a felhasználónév-jelszó párost, amíg a felhasználó mindkettőt hibátlanul meg nem adja. 
A program egyetlen felhasználó (bori99) jelszavát (Szivecske<3) ismeri, csak ezt a párost fogadja el helyesként. 
Mind a sikertelen, mind a sikeres bejelentkezési kísérletekről üzenetet ír a képernyőre.
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Adja meg a felhasználónevét! bori99
Adja meg a jelszavát! Szivecske<3
Belépés engedélyezve.
-----
Adja meg a felhasználónevét! Bagaméri
Adja meg a jelszavát! A kankalin sötétben virágzik!
Belépés megtagadva.
Adja meg a felhasználónevét! bori99
Adja meg a jelszavát! hibásjelszó
Belépés megtagadva.
Adja meg a felhasználónevét! hibásfelhasználó
Adja meg a jelszavát! Szivecske<3
Belépés megtagadva.
Adja meg a felhasználónevét! bori99
Adja meg a jelszavát! Szivecske<3
Belépés engedélyezve.
'''



nev = "bori99"

jelszo = "Szivecske<3"

a = 0
while a <= 0:
    beirtnev = str(input("Adja meg a felhasználónevét! "))
    beirtjelsz = str(input("Adja meg a jelszavát! "))
    if beirtnev == nev and beirtjelsz == jelszo:
        a +=1
        break
    if beirtnev is not nev and beirtjelsz is not jelszo:
        print("siekrtelen bejelentkezés")
        a = 0
print("bejelentkezve")