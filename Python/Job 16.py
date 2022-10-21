# écrit les chiffres dans une liste
list = [int(x) for x in input("entrez 4 chiffres ").split()]

# sépares les éléments dans des variables différentes
var1 = (list[0])
var2 = (list[1])
var3 = (list[2])
var4 = (list[3])

# fonction qui affiche les variables
def myFunction(*arguments):


    print(var1,var2,var3,var4)

myFunction()





