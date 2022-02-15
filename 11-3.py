def triangular_num(n, i = 1, product = 0):
    if i > n:
        return product
    else:
        return triangular_num(n, i+1, product + i)
print(triangular_num(3))