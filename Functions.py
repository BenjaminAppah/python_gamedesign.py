def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return None
    
def is_prime(number):
    if number % 2 != 0:
        return True
    else:
        return None    
    
def check_prime_or_even(number,primeFunc,evenFunc):
    if number < 2:
        print("not prime nor even")
    else:
        if primeFunc(number) != None:
            print(primeFunc(number),"This is a prime number")
        elif evenFunc(number) != None:
            print(evenFunc(number),"This is an even number")

from math import sqrt

def isprime(n):
    if n == 2 or n == 3: return True
    if n == 2 or n % 2 == 0 or n % 3 == 0: return False
    for k in range(5, int(sqrt(n)+1), 2):
        if n % k == 0:
            return False
        return True

print(isprime(7))
print(isprime(11))
print(isprime(15))
print(isprime(107))
print(isprime(127))
print(isprime(3907))
print(isprime(3901))

print(+[i for i in range(100) if isprime(i)])