hauteur = int(input ("Hauteur"))

# -2 pour la premiere et derniere lignes du triangle faite hors de la boucle
compteur=hauteur-2
ecart2 = 1
print(" "*compteur," ","/ \ ")

while compteur!=0:

    ecart1 = compteur
    print(" "*ecart1," /"," "*ecart2,"\ ")
    compteur = compteur-1
    ecart2=ecart2+2

print(" "*ecart1,"/","_"*ecart2,"\ ")