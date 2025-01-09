"""
Koosta programm, mis küsib kasutajalt nime
ja tervitab teda nimeliselt 5 korda ja lisab ka tervituse järjekorranumber.
"""

def solution():
    name = input("Enter your name: ")
    for number in range (5):
        print(f"Ole tervitatud, {name}, {number + 1}. korda.")