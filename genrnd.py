#función genrnd que retorna una lista con 50 números aleatorios.
#material: https://python-para-impacientes.blogspot.com/2015/09/el-modulo-random.html

def genrnd():
    from random import randrange
    lista_aleatoria = []
    #recorremos 50 veces el for para agregar 50 numeros aleatorios de 1 al 100
    for i in range(50):
        #randrange elije un aleatorio en el rango asignado
        lista_aleatoria.append((randrange(1, 101)))
    print(lista_aleatoria)
    return lista_aleatoria
