print("entrer votre texte")
texte = input("texte : ")
print("choisir votre action ( upper / lower / title / clean )")
action = input("action : ")
print("choisir votre methode ( simple ou dure )")
methode = input("methode : ")

#la méthode simple et éfficace (avec fonction system )
def mySimpleUpper(texte):
    print(texte.upper())
def mySimpleLower(texte):
    print(texte.lower())
def mySimpleTitle(texte):
    print(texte.title())
def mySimpleClean(texte):
    print(texte.replace(" ", ""))

#methode sans les fonction system
def myUpper(texte):
    # si il est dans les 26 premieres lettres , il prend la meme lettre dans les 26 dernieres
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
    #si il est dans les 26 premieres lettres , il prend la meme lettre dans les 26 dernieres
    #j'ai juste inversé les deux alphabets ... magik
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

if methode == "simple":
    print("methode simple")
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
elif methode == "dure":
    print("methode dure")
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
    print("pas la bonne methode")