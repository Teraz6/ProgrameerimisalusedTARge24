"""
Koosta programm, mis aitab lastel treenida liitmist.
Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust.
Kui vastus on õige, kiitma kasutajat, kui aga vale, andma õige vastuse ja esitama uue tehte.
Järjest esitatavate tehete hulk võib olla programmis ette antud (näiteks 10),
samuti võib olla ette antud piirid, kui suuri arve kasutajalt küsitakse (näiteks 1 kuni 50).

Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast viimast tehet tulemuse.
"""
from random import randint

# While tsükliga

def sum_exercise():
    counter = 0
    correct_answer = 0
    while counter < 10:
        arv1 = randint(1,50)
        arv2 = randint(1,50)
        tulemus = arv1 + arv2
        counter += 1
        vastus = int(input(f"{counter}. ülesanne: {arv1} + {arv2} = "))
        if vastus == tulemus:
            correct_answer += 1
            print("Tubli, õige vastus")
        else:
            print(f"Sinu vastus oli vale. Õige vastus on {tulemus}")
    print(f"See oli viimane ülesanne. Kogusid 10-st punktist {correct_answer}")

# For tsükliga; lowest,highest, count ei tööta :(

def sum_exercise2(lowest=1, highest=50, count=10):
    correct_counter = 0
    for i in range (count):
        first_number = randint(lowest,highest)
        second_number = randint(lowest,highest)
        random_operator = randint(1,3)
        if random_operator == 1:
            correct_answer = first_number + second_number
            correct_counter = show_equation(first_number, second_number, correct_answer, "+")
        elif random_operator == 2:
            correct_answer = first_number - second_number
            correct_counter = show_equation(first_number, second_number, correct_answer, "-")
        elif random_operator == 3:
            correct_answer = first_number * second_number
            correct_counter = show_equation(first_number, second_number, correct_answer, "*")
    print(f"Your tried {count} times and got {correct_counter} correct answers.")


def show_equation(first_number, second_number, correct_answer,operation_symbol):
    user_answer = int(input(f"{first_number} {operation_symbol} {second_number} = "))
    if user_answer == correct_answer:
        print("Correct answer")
        return 1
    else:
        print("Incorrect answer")
        print(f"{first_number} {operation_symbol} {second_number} = {correct_answer}")
    return 0


if __name__ == "__main__":
    sum_exercise()
    lowest = int(input("Sisesta väikseim täisarv: "))
    highest = int(input("Sisesta suurim täisarv:"))
    count = int(input("Mitu tehet soovid teha? "))
    sum_exercise2()