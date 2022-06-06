def radicacion(a, b):
    # Comprobar que el índice no sea 0
    if b == 0:
        print('Error, el índice de una raiz no puede ser 0')
        return

    # Comprobar si el radicando es negativo y el índice par
    if a < 0 and b % 2 == 0:
        print('No existe la raiz')
        return

    if a < 0 and b % 2 != 0:
        a = a * (-1)
        resultado = - (a ** (1/b))
    else:
        resultado = (a ** (1/b))

    return round(resultado, 4)
