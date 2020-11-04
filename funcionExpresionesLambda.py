def hacer_incrementador(n):
    return lambda x: x + n

f = hacer_incrementador(42)
f(0)
f(1)