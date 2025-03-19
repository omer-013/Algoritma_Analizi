def fibonacci_iterative(n):
    if n <= 0:
        return "Hatali giris. Lutfen 0' dan buyuk bir sayi giriniz."
    elif n == 1:
        return 1

    a = 0
    b = 1
    for i in range(n - 1):
        c = a + b
        a = b
        b = c
    return b