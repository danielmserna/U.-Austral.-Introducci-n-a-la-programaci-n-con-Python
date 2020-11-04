import time

f = lambda x: x+1

print("Tipo de f:", type(f))
print("f(3) = ", f(3))

def function_time(f, *args):
    start_time = time.time()
    result = f(*args)
    end_time = time.time()
    print("Tiempo de ejecucion:", end_time - start_time, "milisegundos")
    return result

print("f(10) = ", function_time(f,10))