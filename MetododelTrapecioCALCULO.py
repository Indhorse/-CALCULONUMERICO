import math

def metodo_trapecio(f, a, b, n):
    """
    Método del trapecio para aproximar la integral definida de una función.

    Parámetros:
    f (función): función a integrar
    a (float): límite inferior de la integral
    b (float): límite superior de la integral
    n (int): número de subintervalos

    Retorna:
    float: aproximación de la integral definida
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]
    integral = h * ((y[0] + y[-1]) / 2 + sum(y[1:-1]))
    return integral

# Ejemplo de uso
def f(x):
    return x**2

a = 0
b = 2
n = 10
aproximacion = metodo_trapecio(f, a, b, n)
print("La aproximación de la integral definida es {:.5f}".format(aproximacion))