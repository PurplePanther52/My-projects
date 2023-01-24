c11 = ""
c12 = ""
c13 = ""
c21 = ""
c22 = ""
c23 = ""
c31 = ""
c32 = ""
c33 = ""
tour = 0
joueur = "X"
etat = ""
while etat == "" and tour < 9:
    print(c11, "|", c12, "|", c13)
    print("---------")
    print(c21, "|", c22, "|", c23)
    print("---------")
    print(c31, "|", c32, "|", c33, "\n")

    if joueur == "X":
        joueur = "O"
    else:
        joueur = "X"

    jouer = False
    while not jouer:
        print("Saisissez les coordonnées de x et y entre 1 et 3.")
        x = int(input("Joueur " + str(joueur) + " donnez votre position en x (horizontal)\n"))
        while x < 1 or x > 3:
            x = int(input("Les coordonnés ne sont pas dans l'intervalle indiquer. Recommencer.\n"))
        y = int(input("et votre position en y (vertical)\n"))
        while y < 1 or y > 3:
            y = int(input("Les coordonnés ne sont pas dans l'intervalle indiquer. Recommencer.\n"))

        if x == 1 and y == 1 and c11 == "":
            c11 = joueur
            jouer = True
        elif x == 1 and y == 2 and c12 == "":
            c12 = joueur
            jouer = True
        elif x == 1 and y == 3 and c13 == "":
            c13 = joueur
            jouer = True
        elif x == 2 and y == 1 and c21 == "":
            c21 = joueur
            jouer = True
        elif x == 2 and y == 2 and c22 == "":
            c22 = joueur
            jouer = True
        elif x == 2 and y == 3 and c23 == "":
            c23 = joueur
            jouer = True
        elif x == 3 and y == 1 and c31 == "":
            c31 = joueur
            jouer = True
        elif x == 3 and y == 2 and c32 == "":
            c32 = joueur
            jouer = True
        elif x == 3 and y == 3 and c33 == "":
            c33 = joueur
            jouer = True
        else:
            print("La case est déja prise. Recommencer.")

    if c11 == c12 and c11 == c13 and c11 == joueur or c21 == c22 and c21 == c23 and c21 == joueur or c31 == c32 and \
            c31 == c33 and c31 == joueur:
        etat = joueur
    elif c11 == c21 and c11 == c31 and c11 == joueur or c12 == c22 and c12 == c32 and c12 == joueur or c13 == c23 and \
            c13 == c33 and c13 == joueur:
        etat = joueur
    elif c11 == c22 and c11 == c33 and c11 == joueur or c13 == c22 and c13 == c31 and c13 == joueur:
        etat = joueur

    tour += 1
if etat == "":
    print("Match nul")
else:
    print("Joueur des pièces", joueur, "gagne!")
