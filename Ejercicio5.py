
# -Transformo la primer letra en numero
# -Primer numero que es procesado
# -Comparo si el numero que estoy procesando ahora es mayor que el ultimo que fue procesado
#    -Si es mayor entonces lo sumo y le resto dos veces el ultimo numero procesado
#    -Si es menor, entonces lo sumo
# -Quito el primer numero y sumo la recursividad

def romano_decimal(nro_romano, ultimo_procesado):
    if (nro_romano == ''):
        return 0
    caracter_actual = nro_romano[0]
    if (caracter_actual == 'I'):
        caracter_actual = 1
    elif (caracter_actual == 'V'):
        caracter_actual = 5
    elif (caracter_actual == 'X'):
        caracter_actual = 10
    elif (caracter_actual == 'L'):
        caracter_actual = 50
    elif (caracter_actual == 'C'):
        caracter_actual = 100
    elif (caracter_actual == 'D'):
        caracter_actual = 500
    elif (caracter_actual == 'M'):
        caracter_actual = 1000

    if (caracter_actual > ultimo_procesado):
        return caracter_actual-ultimo_procesado-ultimo_procesado+romano_decimal(nro_romano[1:], caracter_actual)
    else:
        return caracter_actual + romano_decimal(nro_romano[1:], caracter_actual)


numero_ingresado = (input("Ingrese un numero romano: "))
print('El numero romano en decimal es: ', romano_decimal(numero_ingresado, 0))
