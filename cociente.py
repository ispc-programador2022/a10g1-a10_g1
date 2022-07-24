def div (num1,num2):
    try:
      cociente = num1 / num2
    except  ZeroDivisionError:
       print("No se puede usar 0 para dividir.")#si introduce cero sale este mensaje.#
    except ValueError:
        print("El valor intrucido es erroneo, introduzca un numero.") #Si se introduce una letra sale este except# 
        print("El cociente es  :" , cociente) 
    return cociente
 