import random
import sys
nombre_mystere = random.randrange(0, 100)
chance = 5
tentative = ""
print("*** Le jeu du nombre Mystere ***")

while chance > 0:
    tentative = input("Devine le nombre")
    if int(tentative) == nombre_mystere:
        print("tu as gagne")
        sys.exit("Fin de partie")
    else:
        chance = chance - 1
        if int(tentative) > nombre_mystere:
            print("Le nombre mystere est inferieur")
        elif int(tentative) < nombre_mystere:
            print("Le nombre mystere est superieur")


