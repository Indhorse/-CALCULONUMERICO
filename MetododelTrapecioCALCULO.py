import math

def metodo_trapecio(f, a, b, n):
  
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
