""" Tres amigos están reunidos en un restaurante almorzando. Como dato curioso, uno de ellos comenta que en ese restaurante hacen descuento a mesas donde haya 3 personas, pero para obtener el descuento las edades de los comensales deben cumplir ciertas relaciones entre sí. Una de ellas es que la suma de la edad del que entró primero y la edad del que entró segundo debe dar 5 veces la edad del que entró tercero, y la otra relación es que si se suma dos veces la edad del que entró primero más cuatro da exactamente la edad del que entró segundo al restaurante.

El tipo de descuento está determinado por el rango en el que esté la edad de la persona que entró de ultimas. Si la edad está entre 0 y 20 años el tipo de descuento a aplicar será tipo 1, si la edad está entre 21 y 30 el tipo de descuento a aplicar será el tipo 2, si la edad está entre 31 y 50 el tipo de descuento a aplicar será el tipo 3, y si la edad es mayor o igual a 51 el tipo de descuento a aplicar será el tipo 4.

Elabora un programa que permita, dada la edad del que entró primero al restaurante, conocer las otras dos edades y el tipo de descuento a aplicar.

Entrada
La entrada es la edad del que entró primero al restaurante.

Salida
Tres números enteros separados por espacio que representan las edades del que entró primero, del que entró segundo y del que entró tercero al restaurante. En la siguiente línea debe mostrarse, en letras, el tipo de descuento a aplicar.

 """


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
