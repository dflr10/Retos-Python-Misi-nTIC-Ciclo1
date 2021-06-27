def discountAge(firstAge):
    secondAge = 2*firstAge + 4
    thirdAge = (firstAge+secondAge)//5
    discount = ""
    if thirdAge > 0 and thirdAge < 21:
        discount = "uno"
    elif thirdAge > 20 and thirdAge < 31:
        discount = "dos"
    elif thirdAge > 30 and thirdAge < 51:
        discount = "tres"
    elif thirdAge >= 51:
        discount = "cuatro"
    elif firstAge < 0:
        print("Edad no válida")
        return 0, 0, 0, 0
    return firstAge, secondAge, thirdAge, discount


a, b, c, discount = discountAge(
    int(input("Ingrese la edad del primer comensal: ")))

print(a, b, c, "\n", discount)
