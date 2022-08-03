# getting chi2 table (using inverse chi2 function)
from scipy.stats.distributions import chi2

from random import random


def main():
    err = .05
    m = 2
    n = 3 # cant entidades
    tr = [0 for _ in range(m)]
    tc = [0 for _ in range(n)]
    total = 0

    arr = [[5, 11, 7], [20, 32, 3]]

    # random values
    """
    arr = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = int(round(random()*100,0))
    """

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            tc[j] += arr[i][j]
            tr[i] += arr[i][j]
    total = sum(tr)
    
    ft = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            ft[i][j] = round((tc[j] * tr[i]) / total, 2)

    df = (m - 1) * (n - 1)

    x2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            x2 += (arr[i][j] - ft[i][j]) ** 2 / ft[i][j]

    chi2p = chi2.ppf(1 - err, df=df)
    # chi2p = chi2.cdf(err, df=df)

    res = f" chi2: {round(x2, 2)}, chi2p: {round(chi2p,2)} ... "
    if x2 > chi2p: res += "h0 rechazado"
    else: res += "h1 rechazado"
    
    print(res)

main()