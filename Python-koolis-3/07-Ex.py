"""Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN.
 Seejärel muutke programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d.
X O X
O X O
X O X
 """

def print_square(size):
    for row in range(size):
        for col in range(size):
            print(f"O", end=" ")
        print()


def print_square_with_x(size):
    for row in range(size):
        for col in range(size):
            symbol = "O"
            if row == col or row + col == size - 1:
                symbol = "X"
            print(f"{symbol}", end=" ")
        print()



if __name__ == "__main__":
    size=int(input("Kui suurt ruutu soovid? "))
    print_square(size)
    print("")
    print_square_with_x(size)