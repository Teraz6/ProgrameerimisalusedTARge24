"""
Ülesanne. Saja Aakri mets
Saja Aakri metsa elaniku karupoeg Puhhi fännidest metsaomanikud on oma
metsatükkide pindalad kirjutanud aakrites (1 aaker = 0,4047 hektarit).
Igal omanikul on ainult ühe puuliigi metsad. Konkreetsete puuliikide puhul on
teada aastane metsa juurdekasv hektari kohta tihumeetrites (tm/ha).
Näiteks kase puhul võib see olla 4,8 tm/ha, kuuse puhul 6,6 tm/ha, männi puhul 3,7 tm/ha.
Omanik tahab teada, mitu tihumeetrit metsa aastas teatud suurusest suuremates metsatükkides juurde kasvab.

Koostada funktsioon, mis võtab argumentideks metsatüki pindala (ujukomaarv aakrites)
ja metsa aastase juurdekasvu hektari kohta (ujukomaarv),
tagastab selle pindalaga metsatüki aastase juurdekasvu ümardatuna sajandikeni.

Koostada programm, mis
•	küsib kasutajalt
o	failinime (failis on eraldi ridadel metsatükkide pindalad aakrites);
o	vastava puuliigi aastase juurdekasvu hektari kohta tihumeetrites (ujukomaarv);
o	piiri, mitmest aakrist suuremad metsatükid arvesse võtta (ujukomaarv);
•	loeb failist metsatükkide pindalad;
•	arvutab (funktsiooni abil) ja väljastab metsatüki aastase juurdekasvu,
    kui selle metsatüki pindala on sisestatud piirist suurem;
•	väljastab teate “Metsatükki ei võeta arvesse”, kui metsatüki pindala ei ole sisestatud piirist suurem;
•	väljastab lõpuks ekraanile, mitme metsatüki juurdekasv arvutati.
"""
"""
Näide funktsiooni rakendamisest
 
Näide programmi tööst
Faili andmed.txt sisu:
0.9
3.78
2.05
1.58
"""

def calculate_forest_area(forest_area, yearly_growth):
    forest_area = forest_area * 0.4047
    total_growth = forest_area + yearly_growth
    return round(total_growth, 1)


def open_file():
    filename = input("Sisestage faili nimi: ")
    yearly_growth = float(input("Sisestage aastane juurdekasv hektari kohta: "))
    suitable_area_size = float(input("Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: "))

    with open(filename) as f:
        for line in f:
            forest_area = float(line.strip())
            if forest_area > suitable_area_size:
                total_growth = calculate_forest_area(forest_area, yearly_growth)
                print(f"Metsatükki aastane juurde kasv on {total_growth} hektarit.")
            else:
                print("Metsatükki ei võeta arvesse")


if __name__ == "__main__":
    open_file()