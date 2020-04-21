limit = 75


def isPrime(number):
    if number < 2: return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


for i in range(int(limit) + 1):
    if isPrime(i):
        print(i, end=", ")
