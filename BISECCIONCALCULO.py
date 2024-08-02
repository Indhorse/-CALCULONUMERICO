import math

def biseccion(f, a, b, tol=1e-5, max_iter=100):
    """
    Método de bisección para encontrar raíces de una función.

    Parámetros:
    f (función): función a la que se le busca la raíz
    a (float): límite inferior del intervalo
    b (float): límite superior del intervalo
    tol (float, opcional): tolerancia para la aproximación (default: 1e-5)
    max_iter (int, opcional): número máximo de iteraciones (default: 100)

    Retorna:
    float: aproximación de la raíz
    """
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