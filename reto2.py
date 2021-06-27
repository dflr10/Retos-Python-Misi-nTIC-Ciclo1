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
