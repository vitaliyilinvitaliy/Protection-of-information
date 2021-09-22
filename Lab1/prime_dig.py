import random

def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

def generate_prime(max :int):
    prime_digit = 0;

    while isPrime(prime_digit) == False:
        prime_digit = random.randint(0, 999999)
    
    return prime_digit


