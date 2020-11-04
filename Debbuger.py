def a_function(a_number):

    import pdb
    pdb.set_trace()
    result = None
    if a_number % 2 == 0:
        if a_number % 10 == 0:
            result = a_number / 2
        elif a_number % 8 == 0:
            result = a_number / 4
        else:
            result = a_number - 1
    else:
        if a_number % 3 == 0:
            result = a_number * 11
        elif a_number % 7 == 0:
            result = a_number * 23
        else:
            result = a_number + 1
    return result

result_1 = a_function(20)
print(result_1)

# letra ele (l) para ver las líneas de código
# Ver el valor de una variable escribimos el nombre y presionamos enter
# para continuar con la siguiente linea se hace con la letra n
# si la sentencia actual hace una llamada a una funcion y nos queremos meter dentro de esa funcion oprimimos s
# con c nos vamos al siguiente breakpoint, y sino hay, termina el programa