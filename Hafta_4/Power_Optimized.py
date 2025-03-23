def power_optimized(a, n):
    result = 1
    if(n==1):
        return a
    elif(n%2 == 1):
        return power_optimized(a*a, n/2)*a
    else:
        return power_optimized(a*a, n/2)