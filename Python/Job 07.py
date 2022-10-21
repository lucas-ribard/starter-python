boucle = 1
reste = 0
fizz = 0
buzz = 0

while boucle != 100:
    fizz = 0
    buzz = 0

    # test 3 si modulo = 0 alors le nombre est un multiple de 3
    reste = boucle % 3
    if reste == 0:
        fizz = 1

    # test 5 si modulo = 0 alors le nombre est un multiple de 5
    reste = boucle % 5
    if reste == 0:
        buzz = 1

    # répond en fonction des résultats précédents
    if fizz == 1 and buzz == 1:
        print("FizzBuzz")
    elif fizz == 1 and buzz == 0:
        print("Fizz")
    elif fizz == 0 and buzz == 1:
        print("Buzz")
    else:
        print(boucle)
    boucle = boucle+1
