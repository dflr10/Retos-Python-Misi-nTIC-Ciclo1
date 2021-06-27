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
