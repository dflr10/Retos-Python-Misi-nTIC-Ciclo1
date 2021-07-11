# returns a list whitout elements duplicateds
def clases(A):
    B = []
    for i in A:
        if i not in B:
            B.append(i)
    return B


def mefaltandelaclase(L, M, N):
    output = []
    for element in L:
        if M[element] == N:
            output.append(element)
    return output


def notengo(L_empleado, L_vacunado):
    noVacunado = []
    for empleado in L_empleado:
        if empleado not in L_vacunado:
            noVacunado.append(empleado)
    return noVacunado


def puedocambiar(L_Depto_A, L_Depto_B):
    counter = 0
    counter2 = 0
    for empleado in L_Depto_A:
        if empleado not in L_Depto_B:
            counter += 1

    for empleado in L_Depto_B:
        if empleado not in L_Depto_A:
            counter2 += 1

    return (counter if counter < counter2 else counter2)
