"""
Harjutus 1
Kt 5

    1.       Küsi kasutaja nime
    2.       Kui nimepikkus on vahemikus 5 – 10 (kaasa arvatud), siis tervita 3 korda
    3.       Muidu küsi kolm arvu ja tagasta nende summa. (Kordus)
"""

def greeting(name):
    letter_in_name = len(name)
    if 4 < letter_in_name < 11:
        for i in range(3):
            print(f"Hello, {name}")

    else:
        number_1 = int(input("Insert first number: "))
        number_2 = int(input("Insert second number: "))
        number_3 = int(input("Insert third number: "))
        sum_of_numbers = number_1 + number_2 + number_3
        print(f"Sum of the given numbers are {sum_of_numbers}")


"""
Koostada programm, mis
•küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
•arvutab while-tsükli abil lillede koguarvu, mida pood kingib;
•väljastab saadud lillede arvu ekraanile.
Esimene ostja saab ühe lille, teine ei saa ühtegi, kolmas ostja saab kolm lille jne.
"""

def total_flowers(number):
    client_count = int(number)
    flower_count = 0
    client = 1
    while client <= client_count:
        if client % 2 != 0:
            flower_count += client
        client += 1
    print(f"Total flowers is: {flower_count}")


"""
esimene ostja saab ühe lille, teine ostja saab kolm lille,
kolmas ostja saab viis lille, neljas ostja seitse lille jne.
Koostada programm, mis
•küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
•arvutab while-tsükli abil lillede koguarvu, mida pood klientidele kingib;
•väljastab kingitavate lillede koguarvu.
"""

def total_flowers_2(number):
    client_count = int(number)
    flower_count = 0
    client = 1
    given_flowers = 0
    while client <= client_count:
        flower_count += 2 * client - 1
        client += 1
    print(f"Total flowers is: {given_flowers}")


if __name__ == '__main__':
    greeting(input("What is your name? "))
    total_flowers(input("Enter a number: "))
    total_flowers_2(input("Enter a number: "))

