mylist = [int(x) for x in input("entrez votre liste de nombre").split()]
new_list = []

while mylist:
    min = mylist[0]
    for x in mylist:
        if x < min:
            min = x
    new_list.append(min)
    mylist.remove(min)

print(new_list)