
def decrement_all(numbers:list):
    result = numbers[::]
    for i in range(len(result)):
        result[i] -= 1
    return result

numbers = [1,2,3]
print(f"{numbers=}")
decremented_numbers = decrement_all(numbers)
print(f"{numbers=}")
print(f"{decremented_numbers=}")

# numbrite lisamine listi
numbers.append(5)
numbers += [6]
print(f"{numbers=}")

#numbri lisamine kindlale kohale
numbers [2:2] = [8]
print(f"{numbers=}")

#Eemaldab numbri listist
numbers = [1,2,3,4,5,1]
numbers.remove(1)
print(f"{numbers=}")

#Eemaldab listi, mis sisaldab "4"; (-1) alustab tagant poolt otsimist.
matrix = [[1],[2,3],[4,5,6]]
print(f"{matrix=}")
if [4] in matrix:
    matrix.remove([4])
removed = matrix.pop(-1)
print(f"{matrix=}")
print(f"{removed=}")

# Liidab kõik kokku
print(sum([22, 75, 24, 55]))

# Sorteerib numberid
list_of_numbers = [5,2,7,4,1]
another_list = sorted(list_of_numbers)
print(f"{another_list=}")
print(sorted(list_of_numbers, reverse=True))

# Prindib viimase tähe järgi kõige esimese nime tähestikulises järjekorras
names = ["ago", "mati", "reinuvader", "kasparr", "guido"]
print(min(names, key=lambda x: x[::-1]))

# Prindib viimase tähe järgi kõige esimese nime tähestikulises järjekorras
# .lower muudab sõned väikesteks tähtedeks, muidu oleks "AGO" kõige esimene.
names = ["AGO", "mati", "reinuvader", "kasparr", "guido"]
print(min(names, key=lambda x: x.lower()[::-1]))

