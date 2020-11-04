def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")

loro(1000) # 1 argumento posicional
loro(tension=1000) # 1 argumento nombrado
loro(tension=1000000, accion='VOOOOOM') # 2 argumentos nombrados
loro(accion='VOOOOOM', tension=1000000) # 2 argumentos nombrados
loro('un millón', 'despojado de vida', 'saltar') # 3 args posicionales
loro('mil', estado='viendo crecer las flores desde abajo')