import math


def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raíces de una función.

    Parámetros:
    f (función): función a la que se le busca la raíz
    df (función): derivada de la función f
    x0 (float): aproximación inicial de la raíz
    tol (float, opcional): tolerancia para la aproximación (default: 1e-5)
    max_iter (int, opcional): número máximo de iteraciones (default: 100)

    Retorna:
    float: aproximación de la raíz
    """
    x = x0
    for _ in range(max_iter):
        x_next = x - f(x) / df(x)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next

    raise RuntimeError("No se encontró la raíz después de {} iteraciones".format(max_iter))

# Ejemplo de uso
def f(x):
    return x**2 - 2

def df(x):
    return 2*x

x0 = 1.5
raiz = newton_raphson(f, df, x0)
print("La raíz de la función es aproximadamente {:.5f}".format(raiz))