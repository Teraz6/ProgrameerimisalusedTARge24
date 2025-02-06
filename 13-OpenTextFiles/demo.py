""" Faili operatsioonide demo"""
file_name = "test.txt"

with open("test.txt", "a", encoding="utf8") as file:
    file.write("Tere\n")


with open(file_name, encoding="utf8") as file:
    print(file.readlines())