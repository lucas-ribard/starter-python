age = input('Bonjour, quel age as tu ?')
#transforme age en int, sinon il n'arrive pas a faire de calculs
age = int(age)
if age < 18:
    print("tu est mineur")
else:
    print("tu est majeur")