"""
Ülesanne. Cooperi test

Cooper testis mõõdetakse, kui palju suudab inimene joosta 12 minutiga.
On määratud erinevad hindenormid meestele ja naistele.

Koostada funktsioon, mis võtab argumentideks meetrite arvu ja jooksja soo ning tagastab:
•	Sõne „väga hea“, kui meetreid on meeste puhul vähemalt 2800 ja naiste puhul 2600 vähem
•	Sõne „nõrk“, kui meetreid on meeste puhul vähem kui 2000 ja naistel alla 1800
•	Sõne „rahuldav“ muudel juhtudel
•	Tulemused, mis jäävad alla „väga hea“, peavad lisaks teatama, mitu meetrit jäi järgmisest hindest puudu

Koostada programm, mis küsib kasutajalt:
•	failinime,
Programm peab:
•	lugema failist jooksutulemused (täisarvud) ja jooksjate sood (M või N);
•	funktsiooniga arvutama hinded ja väljastama need ekraanile
•	arvutama ja väljastama ekraanile sugude kaupa kõikide tulemuste täisarvuni ümardatud keskmised
ning funktsiooni abil keskmised hinded.
"""
"""
Näide funktsiooni rakendamisest
>>> hinda(1800,’N’)
’rahuldav, järgmisest hindest puudu 800 m’
>>> hinda(1799,’N’)
’nõrk, järgmisest hindest puudu 1m’
>>> hinda(2600,’N’)
’väga hea’
Näide programmi tööst
Faili cooper.txt sisu:
1900 N
1800 M
2700 M
2600 N
1400 M
3801 N
1500 N
1800 N

Programmi töö:
Sisestage failinimi: cooper.txt
N 1900 m, rahuldav, järgmisest hindest puudu 700 m
M 1800 m, nõrk, järgmisest hindest puudu 200 m
M 2700 m, rahuldav, järgmisest hindest puudu 100 m
N 2600 m, väga hea
M 1400 m, nõrk, järgmisest hindest puudu 600 m
N 3801 m, väga hea
N 1500 m, nõrk, järgmisest hindest puudu 300 m
N 1800 m, rahuldav, järgmisest hindest puudu 800 m
Keskmised:
M 1967 m, nõrk, järgmisest hindest puudu 33 m
N 2320 m, rahuldav, järgmisest hindest puudu 280 m
"""

def calculate_grade(distance, gender):
    if gender == "M":
        if distance >= 2800:
            print(f"{gender} {distance} m, väga hea")
        elif distance < 2000:
            print(f"{gender} {distance} m, nõrk, järgmisest hindest on puudu {2000 - distance}m")
        else:
            print(f"{gender} {distance} m, rahuldav, järgmisest hindest on puudu {2800 - distance}m")

    if gender == "N":
        if distance >= 2600:
            print(f"{gender} {distance} m, väga hea")
        elif distance < 1800:
            print(f"{gender} {distance} m, nõrk, järgmisest hindest on puudu {1800 - distance}m")
        else:
            print(f"{gender} {distance} m, rahuldav, järgmisest hindest on puudu {2600 - distance}m")

def average_grade(results):
    m_distance = 0
    m_count = 0
    n_distance = 0
    n_count = 0

    for distance, gender in results:
        if gender == "M":
            m_distance += distance
            m_count += 1
        elif gender == "N":
            n_distance += distance
            n_count += 1

    print("Keskmised:")

    if m_count > 0:
        m_avg = m_distance / m_count
        m_avg = round(m_avg)
        print(calculate_grade(m_avg, "M"))

    if n_count > 0:
        n_avg = n_distance / n_count
        n_avg = round(n_avg)
        return calculate_grade(n_avg, "N")


def read_data_from_file():
    filename = input("Sisesta faili nimi koos faili vormiga (.txt): ")
    results = []
    with open(filename, "r") as file:
        for line in file:
            distance, gender = line.strip().split(" ")
            distance = int(distance)
            results.append((distance, gender))
            calculate_grade(distance, gender)

        average_grade(results)


if __name__ == "__main__":
    read_data_from_file()
