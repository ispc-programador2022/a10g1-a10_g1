def funcionPotencia():
    param1 = float(input("introduzca un número: "))
    param2 = float(input("introduzca el número que desea que sea la potencia del anterior: "))
    resultadoPotencia = round(param1**param2, 4)
    print(resultadoPotencia)
    return resultadoPotencia