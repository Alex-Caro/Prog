def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a



def is_prime(n):
    if n < 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    for a in range(2, n):
        if n % a == 0:
            return False
    return True



def print_prime_factors(n):
    print(n,"=", end=" ")
    for i in range(2,n+1):
        while n % i == 0:
            print(i, end=" ")
            n=n/i
            if n == 1:
                print("", end="")
            else:
                print("*", end=" ")

