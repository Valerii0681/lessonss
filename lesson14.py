def digProd(n):
    if (n < 10):
        if (n == 0):
            return 1
        else:
            return n
    else:
        k = n % 10
        if (k == 0):
            k = 1
        return k * digProd(n // 10)


print(digProd(1230097))