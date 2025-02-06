print(type((1,2) + (3,)))

# Tuple(ennik) kasutamine võtmena, sellele väärtuse määramine ja uute võtmete lisamine dictionarysse
points = {(-1, -1): "B"}
points[(1, 2)] = "A"
points[(0, 0)] = "Center"
points[(2, 1)] = "Delta"
print(points)

# KEY määramine tuple's olevate arvudele
ennnik = (1, 2, 3)
üks, kaks, kolm = ennnik

