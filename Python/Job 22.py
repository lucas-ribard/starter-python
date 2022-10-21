print("entrer votre texte")
texte = input("texte : ")
print("choisir votre action : \"upper\" \"lower\" \"title\" \"clean\" ")
action = input("action : ")
print("choisir votre methode : \"avec\" ou \"sans\" fonction system ")
methode = input("methode : ")

# la méthode simple et éfficace (avec fonction system )
def mySimpleUpper(texte):
    print(texte.upper())
def mySimpleLower(texte):
    print(texte.lower())
def mySimpleTitle(texte):
    print(texte.title())
def mySimpleClean(texte):
    #remplace les espaces par du vide
    print(texte.replace(" ", ""))

# methode sans les fonctions system
def myUpper(texte):
    # si il est dans les 26 premieres lettres, il prend la meme lettre dans les 26 dernieres
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for x in texte:
        for pos in range(52):
            if alphabet[pos] == x:
                i = pos
        if x not in alphabet or i >= 26:
            result += x
        else:
            result += alphabet[i + 26]
    return result
    #bruh

def myLower(texte):
    # si il est dans les 26 premieres lettres, il prend la meme lettre dans les 26 dernieres
    # j'ai juste inversé les deux alphabets ... magik
    # on aurait pu changer les code pour qu'il fasse l'opposé, mais c'est plus long
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = ''
    for x in texte:
        for pos in range(52):
            if alphabet[pos] == x:
                i = pos
        if x not in alphabet or i >= 26:
            result += x
        else:
            result += alphabet[i + 26]
    return result
    # ez

def myTitle(texte):
    print("Pas encore fait")
    return result

def myClean(texte):
    print("pas encore fait")
    return result

if methode == "avec":
    print("avec fonction system")
    if action == "upper":
        mySimpleUpper(texte)


    elif action == "lower":
        mySimpleLower(texte)

    elif action == "title":
        mySimpleTitle(texte)

    elif action == "clean":
        mySimpleClean(texte)

    else:
        print("Action non reconnue")


#la méthode moins simple
elif methode == "sans":
    print("sans fonction system")
    if action == "upper":
        result=myUpper(texte)
        print(result)
    elif action == "lower":
        result=myLower(texte)
        print(result)
    elif action == "title":
        result=myTitle(texte)
        print(result)
    elif action == "clean":
        result=myClean(texte)
        print(result)
    else:
        print("Action non reconnue")

else:
    print("veuillez écrire \"avec\" ou \"sans\"")