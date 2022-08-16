# Crear función módulo. Debe tomar como parámetro dos números y devolver su módulo.
def modulo(a, b):
    if b == 0:
        return 'El divisor no puede ser cero'
    else:
        return a % b
