import math


def factorial(n):
    if n < 2: return 1
    return n * factorial(n - 1)


def poisson(u, x):
    return (math.e ** -u *u**x) / factorial(x)


def main():
    u = 4
    x_list = list(range(10))
    for x in x_list:
        print(f"f({x}) = P(X = {x}) = {round(poisson(u, x), 6)}")


main()