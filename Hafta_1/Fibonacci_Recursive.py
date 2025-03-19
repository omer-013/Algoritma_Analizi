def fibonacci_recursive(n):
    if n <= 0:
        return "Hatali giris. Lutfen 0' dan buyuk bir sayi giriniz."
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
