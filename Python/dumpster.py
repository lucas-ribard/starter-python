texte="Bippity Bopity, ur code is now my PROPRETY"
def myUpper(texte):

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


print(myUpper(texte))