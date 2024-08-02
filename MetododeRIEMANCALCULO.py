def riemann_integration(f, a, b, n, method='left'):
    """
    Método de integración de Riemann para aproximar la integral definida de una función.

    Parámetros:
    f (función): función a integrar
    a (float): límite inferior de la integral
    b (float): límite superior de la integral
    n (int): número de subintervalos
    method (str): método de integración (left, right, midpoint)

    Retorna:
    float: aproximación de la integral definida
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]

    if method == 'left':
        y = [f(xi) for xi in x[:-1]]
    elif method == 'right':
        y = [f(xi) for xi in x[1:]]
    elif method == 'idpoint':
        y = [f((xi + xi + h) / 2) for xi in x[:-1]]
    else:
        raise ValueError("Method must be 'left', 'right', or 'idpoint'")

    integral = h * sum(y)
    return integral

# Ejemplo de uso
def f(x):
    return x**2

a = 0
b = 2
n = 10
method = 'idpoint'

aproximacion = riemann_integration(f, a, b, n, method)
print("La aproximación de la integral definida es {:.5f}".format(aproximacion))