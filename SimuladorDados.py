import random

def funcion_tira_dados():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    suma = d1 + d2
    
    print("El primer dado da como resultado: ",d1)
    print("El segundo dado da como resultado: ",d2)
    print("La suma de los dados es: ",suma)
    
    decision = input("¿Deseas tirar los dados nuevamente? (Responde 'Si' si quieres seguir jugando)")

    if decision == "si" or decision == "Si" or decision == "SI" or decision == "sI":
        funcion_tira_dados()
    else:
        print("Jugaremos en otra ocasion")

