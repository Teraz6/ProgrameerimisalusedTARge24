counter = 0
for x in range(1,21):
    for y in range(1,21):
        for z in range(1,21):
            print(f"{x} - {y} - {z}")
            counter += 1
print(f"Kokku leiti {counter} kombinatsiooni")