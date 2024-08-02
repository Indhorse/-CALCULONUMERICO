import math

def taylor_series(f, x0, x, n):
   
    resultado = 0
    for i in range(n):
        derivada = derivada_n(f, x0, i)
        resultado += (derivada / math.factorial(i)) * (x - x0)**i
    return resultado

def derivada_n(f, x0, n):
  
    if n == 0:
        return f(x0)
    else:
        h = 1e-6
        return (derivada_n(f, x0 + h, n - 1) - derivada_n(f, x0 - h, n - 1)) / (2 * h)

# Ejemplo de uso
def f(x):
    return math.exp(x)

x0 = 0
x = 1
n = 10
aproximacion = taylor_series(f, x0, x, n)
print("La aproximación de la función en el punto x={} es {:.5f}".format(x, aproximacion))
