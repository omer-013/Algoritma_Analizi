def power(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a

    return result