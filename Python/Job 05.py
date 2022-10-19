Valeur1 = input('Valeur 1 :')
Valeur1 = int(Valeur1)
Valeur2 = input('Valeur 2 :')
Valeur2 = int(Valeur2)
temp = 0

if Valeur1 < Valeur2:
    temp = Valeur1 + 1

    while temp != Valeur2:
        print(temp)
        temp = temp + 1

elif Valeur2 < Valeur1:
    temp = Valeur1 - 1

    while temp != Valeur2:
        print(temp)
        temp = temp - 1

elif Valeur1 == Valeur2:
    print("Valeurs égales")
