def radicacion(a, b):
    try:
        b = 1 / b
        # Comprobar si el radicando es negativo y el índice par
        if a < 0 and b % 2 == 0:
            return 'No existe la raiz'
        elif a < 0 and b % 2 != 0:
            a = a * -1
            resultado = - (a ** b)
        else:
            resultado = (a ** b)

        return round(resultado, 4)

    # Excepción para índice no sea 0
    except ZeroDivisionError:
        return 'Error, el índice de una raiz no puede ser 0'
    except Exception as e:
        return e
