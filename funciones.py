def peso(masa,gravedad =9.8):
    "Fórmula del peso"
    return masa*gravedad

#Parámetros opcionales
print("Peso en la tierra:", peso(10))
print("Peso en la luna",peso(10,1.63))

def suma_numeros(*args):
    "Suma los numeros pasados por parámetros"
    return sum(args)

print("6 + 7 + 8 =", suma_numeros(*[6,7,8]))
print("6 + 7 + 8 =", suma_numeros(6,7,8))

def imprimir_ticket(*args, **kwargs):
    "Imprime el ticket de una compra"
    print("Detalle ticket")
    for item, precio in kwargs.items():
        print(item, ":", precio)

print(imprimir_ticket(6,7))
print(imprimir_ticket((6,7),(8,9)))
