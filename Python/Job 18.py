# nombre à mettre dans la liste
var1 = int(input("premier chiffre"))
var2 = int(input("deuxieme chiffre"))
var3 = int(input("troisieme chiffre"))
var4 = int(input("quatireme chiffre"))

def autosort(*parametres):

    list = []
    list.append(var1)
    list.append(var2)
    list.append(var3)
    list.append(var4)
    list.sort()
    print(list)

autosort()