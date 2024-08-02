import math

def biseccion(f, a, b, tol=1e-5, max_iter=100):
  
    if f(a) * f(b) > 0:
        raise ValueError("La función no cambia de signo en el intervalo")

    for _ in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    raise RuntimeError("No se encontró la raíz después de {} iteraciones".format(max_iter))

# Ejemplo de uso
def f(x):
    return x**2 - 2

a = 0
b = 2
raiz = biseccion(f, a, b)
print("La raíz de la función es aproximadamente {:.5f}".format(raiz))
