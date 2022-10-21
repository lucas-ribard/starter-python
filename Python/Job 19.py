# nombre à mettre dans la liste
var1 = int(input("premier chiffre"))
var2 = int(input("deuxieme chiffre"))
var3 = int(input("troisieme chiffre"))
var4 = int(input("quatireme chiffre"))
# pas sûr que c'est la bonne méthode, mais je n'ai pas vraiment compris l'énoncé

def autosort(*parametres):

    list = []
    # ajoute les var à la liste
    list.append(var1)
    list.append(var2)
    list.append(var3)
    list.append(var4)
    # nouvelle liste
    liste_ordonné = []

    # ordonne les valeurs sans utiliser sort
    while list:
        min = list[0]
        for x in list:
            if x < min:
                min = x
        liste_ordonné.append(min)
        list.remove(min)

    # la liste finale est : listeordonné
    # mais on peut faire mylist=listordonné
    # pour afficher mylist à la fin

    print(liste_ordonné)

autosort()