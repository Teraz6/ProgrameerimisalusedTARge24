"""
Ülesanne. Kaltsuvaip
Tõenäoliselt on paljud näinud kaltsuvaipu, kuid võib-olla pole mõelnud sellele,
kuidas neid valmistatakse. Kaltsuvaipu kootakse spetsiaalsetel telgedel,
millele kinnitatakse hulk tugevast materjalist niite ehk lõimi,
mille vahele hakatakse põimima kaltsuribasid. Lõimed on järgneval joonisel kujutatud rohelisena.
Meie eesmärk on vajaliku lõimeniidi kogupikkuse leidmine.
Kuna lõimed on telgedel pinges, siis pärast valmimist tõmbub vaip mõnevõrra kokku.
Kokku tõmbumise kompenseerimiseks võetakse vaiba algpikkus soovitavast lõpp-pikkusest 20% suurem.
Samuti arvestatakse, et iga lõime kumbagi otsa tuleb jätta sidumiseks 25 cm varu.
Lõimede vahele põimitav materjal (joonisel must) meid siin ei huvita.

Koostada funktsioon, mis võtab argumentideks vaiba lõpp-pikkuse (ujukomaarv) ja lõimede arvu (täisarv),
•	arvutab ja tagastab vaiba lõimede kogupikkuse ümardatuna sajandikeni.

Koostada programm, mis
•	küsib kasutajalt
o	failinime, kus on vaipade lõpp-pikkused ujukomaarvudena meetrites eraldi ridadel,
o	kõrvuti olevate lõimede arvu 5-meetriste ja pikemate vaipade puhul (täisarv),
o	kõrvuti olevate lõimede arvu lühemate vaipade puhul (täisarv);
•	loeb failist vaipade pikkused,
•	arvutab (funktsiooni abil) ja väljastab ekraanile iga vaiba lõimede kogupikkuse,
•	arvutab ja väljastab ekraanile, kui palju läheb lõimeniiti vaja kõigi vaipade
peale kokku ümardatuna sajandikeni.
"""
"""
Näide arvutuskäigust
Olgu näiteks uues hoones tahtmine kasutada kaltsuvaipu lõpp-pikkustega 7 m, 4,9 m, 3,63 m ja 5 m.
Seejuures 5-meetriste või pikemate lõpp-pikkustega vaipade puhul olgu lõimi kõrvuti 120 (vaiba laius umbes 70 cm),
lühemate puhul 140 (vaiba laius umbes 80 cm).
Esimese vaiba üks lõim on pikkusega 7 * 1,2 + 0,5 = 8,9 meetrit.
Kokku on sellel vaibal lõimi 120, sest vaiba pikkus on 5 meetrit või rohkem.
Seega kulub selle vaiba peale kokku 8,9 * 120 = 1068 meetrit lõimeniiti.
Teise, kolmanda ja neljanda vaiba peale kulub vastavalt 893,2; 679,84 ja 780 meetrit.
Järelikult on kõikide vaipade jaoks vaja kokku 1068 + 893,2 + 679,84 + 780 = 3421,04 meetrit lõimeniiti.

Näide funktsiooni rakendamisest
>>> lõimede_pikkus(7, 120)
1068.0

Näide programmi tööst
Faili delta_vaibad.txt sisu:
7
4.9
3.63
5
"""