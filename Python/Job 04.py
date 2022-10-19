nb_loop = input('nombre de boucle :')
#transforme nb_loop en int, sinon il n'arrive pas a faire de calculs
nb_loop = int(nb_loop)
compteur=0

while compteur != nb_loop+1:
    print(compteur)
    compteur=compteur+1

print("boucle finie")