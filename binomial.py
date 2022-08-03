# Resolucion de combinatoria (metodo sin factorial)
def comb(n, x):
    v = 0
    up = 1
    down = 1

    if n - x < x: v = n - x
    else: v = x

    for i in range(n, n - v, -1): up *= i
    for i in range(1, 1 + v): down *= i
    
    return up / down


# func dist Binomial
def binomFx(n, x, p):
    return comb(n, x) * p**x * (1-p)**(n - x)


def main():
    n = 5
    p = .8
    x_list = list(range(n + 1)) # data
    
    for x in x_list:
        print(f"f({x}) = P(X = {x}) = {round(binomFx(n, x, p), 4)}")


main()