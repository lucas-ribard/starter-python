texte = input("entrer un texte : ")

# r, pour une ouverture en lecture (READ).
# w, pour une ouverture en écriture (WRITE), à chaque ouverture le contenu du fichier est écrasé. Si le fichier n'existe pas python le crée.
# a, pour une ouverture en mode ajout à la fin du fichier (APPEND). Si le fichier n'existe pas python le crée.
# b, pour une ouverture en mode binaire.
# t, pour une ouverture en mode texte.
# x, crée un nouveau fichier et l'ouvre pour écriture

fichier = open("Fichier annexes/output.txt", "w")
fichier.write( texte)
fichier.close()
print("écriture réussite")