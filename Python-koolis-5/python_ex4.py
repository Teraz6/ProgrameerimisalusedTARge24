"""
Lisa kõikidesse sõnastikesse järgmised sõnad:

    headaega - goodbye - arrivederci
    pott - pot - pentola
    sõnastik - dictionary - dizionario

    Tõlgi (väljastage ekraanile) järgmised sõnad:

    üks -> itaalia
    ciao - > eesti
    dog -> itaalia
    pentola - inglise
"""
from python_ex3 import e_italian, e_english
from python_ex3 import second

def add_new_word(estonian, english, italian):
    second.dictionary.english[estonian] = english
    second.dictionary.italian[estonian] = italian
    e_italian[italian] = estonian
    e_english[english] = estonian

add_new_word("headaega", "goodbye", "arrivederci")
add_new_word("pott", "pot", "pentola")
add_new_word("sõnastik", "dictionary", "dizionario")



if __name__ == "__main__":
    """
    Tõlgi (väljastage ekraanile) järgmised sõnad:
    üks -> itaalia
    ciao - > eesti
    dog -> itaalia
    pentola - inglise
    """
    print(f"üks -> itaalia = {second.dictionary.italian['üks']}")
    print(f"ciao -> eesti = {e_italian['ciao']}")
    print(f"dog -> itaalia = {second.dictionary.italian[e_english['dog']]}")
    print(f"pentola -> inglise = {second.dictionary.english[e_italian['pentola']]}")