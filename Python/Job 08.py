hauteur = int(input ("Hauteur"))
largeur = int(input ("Largeur"))


print("|","-"*largeur,"|")
hauteur = hauteur-2
while hauteur !=0:
    print("|"," "*largeur,"|")
    hauteur= hauteur-1
print("|","-"*largeur,"|")