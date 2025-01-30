"""
1.	Küsi kasutajalt 1 arv mille paned astmele 2, 3 ,4 ja 5 kasutades kordust ja järjendit
2.	Lase kasutajal arvata, millises astmes on suvaline arv järjendis
3.	Teata kas arvati õigesti ja kuva õige vastus
4.	Peale seda küsi kasutajalt kas ta soovib teise arvuga programmi korrata või lõpetada. (Kordus)
"""
import random


def guess_number(number):
    """
    :param number: Küsime kasutajalt täisarvu.
    :param user_guess_power: Laseme kasutajal arvata (2-5), mis astmesse numbri panime
    :return: Õige vastuse korral anname võimaluse programmi korrata.
    Vale vastuse korral peab kasutaja uuesti arvama.
    """
    power_list = [2, 3, 4, 5]
    random_number = random.choice(power_list)
    while True:
        user_guess_power = int(input("Arva, mis astmes sinu number pandi(2-5)?: "))
        if user_guess_power == random_number:
            print("Tubli sa arvasid õigesti!")
            print(f"Sinu arv astmes {random_number} = {number ** random_number}!")
            text_answer = input("Kas soovid teise arvuga programmi korrata?(Y/N) ")
            if text_answer == "Y" or "y":
                #Nõustumise korral genereeritakse uuesti suvaline astendaja listist ja küsitakse uut täisarvu
                random_number = random.choice(power_list)
                number = int(input("Sisesta täisarv: "))
                continue
            else:
                #Keeldumisel programm sulgub ja soovib kasutajale "Head aega"
                print("Head aega")
                break
        else:
            print("Vale vastus, proovi uuesti!")


if __name__ == '__main__':
    print(guess_number(int(input("Sisesta täisarv: "))))