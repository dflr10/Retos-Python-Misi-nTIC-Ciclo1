""" Pedro, jefe del área de sistemas, está tratando de medir quién de sus tres empleados que trabajan para él(Diego, Aura y Daniel) llega más veces tarde consecutivamente. Para ello idea un programa en Python que recibe el nombre de la persona que llega tarde cada día. El programa se encarga de contar cuántas veces consecutivamente llega sus empleados a lo largo de varios días.

Entrada
La entrada debe ser el nombre del empleado que llega tarde cada día. Estos nombres deben ir separadas por espacio.

Salida
Se deben generar dos salidas, la primera son los nombres de los empleados, separados por espacios, en el orden en que llegaron tarde.  La segunda línea es el conteo de las veces seguidas que llegó tarde cada empleado. """


def thirdChallenge(employees):
    employees = employees.split()
    times = 1
    output1 = []
    output2 = []
    for i in range(len(employees)-1):
        if employees[i] == employees[i+1]:
            times += 1
        else:
            output1.append(employees[i])
            output2.append(times)
            times = 1
        if i+1 >= len(employees)-1:
            output1.append(employees[i+1])
            output2.append(times)

    names = " ".join(output1)
    later = " ".join((map(str, output2)))
    return print(names, "\n", later)


employees = input("Ingresa los empleados: ")
thirdChallenge(employees)
