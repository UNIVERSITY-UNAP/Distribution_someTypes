import math


# func dist normal
def normal(x, u, o):
    z = (x - u) / o
    fx = math.exp(-.5 * z * 2) / (((2 * math.pi) * .5) * o)
    return round(fx, 9)


# Calculo de la integral por metodo numerico regla del trapecio
def integralTrapz(a, b, u, o, n=1000):
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + i * h
        w = 2
        if i == 0 or i == n - 1:
            w = 1
        s = s + w * normal(x, u, o)
    s = s * h / 2
    return s


# retorna la probabilidad (area total dividida en 4, simetrico a la izquierda)
def distz(z):
    u = 0
    o = 1
    A = [0, integralTrapz(0, z, u, o)]
    A[0] = 1 - A[1]
    return A


def main():
    # datos iniciales (plano XY)
    x = 0
    u = 0
    o = 1
    z = (x - u) / o
    print(distz(z))


main()
