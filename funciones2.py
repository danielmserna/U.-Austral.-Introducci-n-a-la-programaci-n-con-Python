def fib2(n): # devuelve la serie de Fibonacci hasta n
    """Devuelve una lista conteniendo la serie de Fibonacci hasta n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a) # ver abajo
        a, b = b, a+b
    return result

f100 = fib2(100) # llamarla
f100 
print (f100)