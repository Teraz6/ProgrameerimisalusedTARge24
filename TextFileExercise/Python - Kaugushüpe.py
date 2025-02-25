"""
Ülesanne. Kaugushüpe
Noorte kaugushüppe võistlusel sai täita meistrivõistluste normatiivi. Juhtus aga,
et mõõteseade muutis kõiki tulemusi ühe ja sama arvu sentimeetrite võrra.
Õnneks olid tulemused faili salvestatud ja nüüd sai arvutades leida tegelikud tulemused.
Selleks, et edaspidi saaks selliseid olukordi kiiremini lahendada, otsustati tellida programm,
mis lisaks tulemuste korrigeerimisele leiab ka normatiivi täitnud tegelike tulemuste arvu
ning nende aritmeetilise keskmise.
Koostada funktsioon, mis võtab argumentideks vigase tulemuse (meetrites) ja mõõteparanduse (sentimeetrites).

Funktsioon arvutab tegeliku tulemuse (meetrites) ning tagastab selle.
tegelikTulemus = viganeTulemus + mõõteparandus / 100

Koostada programm, mis küsib kasutajalt:
•	failinime,
•	mõõteparanduse (nt 35 näitab, et igale tulemusele tuleb liita 35 sentimeetrit (e 0,35 meetrit)),
•	meistrivõistluste normatiivi.

Programm peab
•	lugema failist vigased tulemused (meetrites);
•	funktsiooniga arvutama tegelikud tulemused ja väljastama need ekraanile
(ümardatuna kahe kümnendkohani pärast koma);
•	arvutama ja väljastama ekraanile normatiivi täitnud tegelike tulemuste arvu
ja nende keskmise (ümardatuna kahe kümnendkohani pärast koma).
o	Kui normatiivi täitjaid ei ole, siis keskmist ei arvutata ega väljastata.
"""
import sys

"""
Näide programmi tööst
Faili kaugus.txt sisu:
6.56
5.76
5.82
5.23
5.74
6.14
5.28
5.77
6.45
6.02
5.78

Programmi töö:
Sisestage failinimi: kaugus.txt
Sisestage parandus sentimeetrites: 35
Sisestage meistrivõistluste normatiiv meetrites: 6.45
Tegelikud tulemused
6.91
6.11
6.17
5.58
6.09
6.49
5.63
6.12
6.8
6.37
6.13
Normatiivi täitis 3.
Täitnute keskmine on 6.73.
"""

def correct_distance(wrong_distance, fix_in_metres):
    actual_distance = round(wrong_distance + fix_in_metres, 2)
    return actual_distance


def open_file():
    filename = input("Sisestage failinimi: ")
    fix_in_centimetres = float(input("Sisestage parandus sentimeetrites: "))
    normative_in_metres = float(input("Sisestage normatiiv meetrites: "))
    fix_in_metres = round(float(fix_in_centimetres * 0.01),2)

    with open(filename) as f:
        print("Tegelikud tulemused:")
        normative_count = 0
        normative_total_in_metres = 0
        actual_distance = 0
        for line in f:
            wrong_distance = float(line.strip())
            actual_distance = correct_distance(wrong_distance, fix_in_metres)
            if actual_distance >= normative_in_metres:
                normative_count += 1
                normative_total_in_metres += actual_distance
            print(actual_distance)
        print(f"Normatiivi täitis {normative_count} võistlejat.")
        print(f"Täitnute keskmine on {round(normative_total_in_metres / normative_count, 2)}.")


if __name__ == "__main__":
    open_file()