x = open("Fichier annexes/domains.xml", "r")
list = []
lignes = x.readlines()

for line in lignes:
    line = line.replace("</column>\n", "")
    list.append(line)
x.close()

list2 = [s for s in list if '<column name="domain">' in s]
print(len(list2))