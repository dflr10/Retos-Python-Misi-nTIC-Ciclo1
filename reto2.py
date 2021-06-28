""" Suponga que usted está con un amigo en una reunión y deciden hacer una apuesta la cual consiste en adivinar la primera letra del nombre de cada persona que vaya entrando a la reunión.

Para ello cada uno debe proponer una lista de letras(puede ser de 3 a 6 letras) antes de empezar la apuesta. Cada vez que entre una persona se mira quién de los dos tiene la letra inicial del nombre de la persona y se sacan las cuentas.

Si usted lleva la ventaja entonces se anota un 1, si su amigo lleva la ventaja entonces se anota un 2, si van empatados entonces se coloca un asterisco.

Realizar un programa que pida las letras que usted propone y las letras que propone su amigo(como cadena de caracteres) y que también pida una cadena de caracteres con la primera letra del nombre de las diferentes personas que entran a la reunión.

Finalmente, se debe mostrar lo que se anota a medida que van entrando las personas.

Entrada
La primera entrada es la lista de letras que usted propone. La segunda entrada es la lista de letras que su amigo propone. La tercera entrada es la lista de iniciales de los nombres de personas que llegan a la reunión.

Salida
La salida es la lista de lo que van anotando a medida que van entrando las personas. """


def secondChallenge(myLetters, friendLetters, peopleFistLetters):
    myPoints = 0
    friendPoints = 0
    output = ""

    for letter in peopleFistLetters:
        if letter in myLetters:
            myPoints += 1
        else:
            myPoints += 0

        if letter in friendLetters:
            friendPoints += 1
        else:
            friendPoints += 0

        if myPoints > friendPoints:
            output += "1"
        elif friendPoints > myPoints:
            output += "2"
        else:
            output += "*"

    return output


print(secondChallenge(input("Ingresa tus letras propuestas: "), input("Ingresa las letras propuestas por tu amigo: "),
      input("Ingresa la primera letra del nombre de las personas que entran a la reunión: ")))
