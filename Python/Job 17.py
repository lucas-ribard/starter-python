#ecrit les chiffre dans une liste
list = [int(x) for x in input("entrez votre liste de nombre").split()]

#cree une deuxieme liste pour afficher les nombre paires
listepaire=[]

#place dans la liste
place=0

#nombre d'éléments dans la liste
nb_elements=len(list)

#le nombre qui est testé
nb_observé=0

#tant que tout les chiffres n'ont pas été testé
while place != nb_elements:
    #prend la valeur du chiffre en position [place] dans la liste
    nb_observé=(list[place])
    
    if nb_observé % 2 == 0:
        #ajoute le nombre a la liste de nombres paires
        listepaire.append(nb_observé)

    place= place+1
#affiche la liste des nombre paires
print("Nombres paires de la liste : ",listepaire)