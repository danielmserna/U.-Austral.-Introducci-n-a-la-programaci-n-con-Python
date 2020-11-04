def f(jamon: str, huevos: str = 'huevos') -> str:
    print("Anotaciones:", f.__annotations__)
    print("Argumentos:", jamon, huevos)
    return jamon + ' y ' + huevos

f('carne')
