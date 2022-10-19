# nombre a mettre dans la liste
var1 = int(input("premier chiffre"))
var2 = int(input("deuxieme chiffre"))
var3 = int(input("troisieme chiffre"))
var4 = int(input("quatireme chiffre"))
#pas sur que c'est la bonne méthode mais j'ai pas vraiment compris l'énoncé

def autosort(*parametres):
    list = []
    liste_ordonné = []

    # ajoute les var a la liste
    list.append(var1)
    list.append(var2)
    list.append(var3)
    list.append(var4)

    # ordonne les valeurs sans utiliser sort
    while list:
        min = list[0]
        for x in list:
            if x < min:
                min = x
        liste_ordonné.append(min)
        list.remove(min)

    return(liste_ordonné)


def myDisplay(liste_ordonné):
    print(liste_ordonné)



liste_ordonné=autosort()
myDisplay(liste_ordonné)
