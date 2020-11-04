def buscar_numero_en(numero, lista):
    for i, item in enumerate(lista):
        if item == numero:
            indice = i
            break
    else:
        indice = -1
    return indice

buscar_numero_en(1, [2,3,1,4,5])
buscar_numero_en(1, [2,6,3,4,5])