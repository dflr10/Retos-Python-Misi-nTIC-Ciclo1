""" Suponga que usted tiene un bar y desea mejorar el surtido de licores. Para eso va a la licorería más cercana con la lista de licores que quiere comprar. La vendedora, quien está aprendiendo a programar en Python, creó un programa que le pide inicialmente los productos con su precio respectivo, en dólares. Luego, el programa pide la lista de los licores que el cliente desea comprar y al final el programa muestra el total a pagar y los licores comprados, según la disponibilidad. Los licores que se manejan son los siguientes:

1) Cerveza    2) Vino    3) Whisky    4) Ron    5) Tequila    6) Aguardiente    7) Vodka    8) Brandi    9) Sangria
    ¿Cómo podría ser el programa que la vendedora hizo?
    Consejo: use un método del módulo json para convertir la primera entrada en diccionario.

    Entradas

    La primera entrada debe ser una cadena de caracteres, que tenga estructura de diccionario donde la llave sea el nombre del producto y el valor el precio. Este diccionario solo contiene los licores que están disponibles en el momento. La segunda entrada debe ser los nombres de los productos que el cliente quiere, separados por espacio.

    Salidas

    La primera salida es el total de los productos comprados, asumiendo que solo compró de a una unidad. La segunda salida es la lista de productos que se pudieron comprar finalmente separados por espacios.
"""
import json


def fourthChallenge(drinks, buys):
    output1 = 0
    output2 = []
    drinks = json.loads(drinks)
    buys = buys.split()

    for buy in buys:
        if buy in drinks:
            output1 += drinks[buy]
            output2.append(buy)

    return(print(output1), '\n', print(" ".join(output2)))


fourthChallenge(input("Ingrese los licores disponibles: "),
                input("Ingrese su compra: "))
