
def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes():  
    for n in range(100):
        if isprime(n):
            print(n,end=" ")
    print()
list_primes()


# another way
def isPrime(n):
    prime = True
    #n's square root = n**.5   
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            prime = False
    return prime

