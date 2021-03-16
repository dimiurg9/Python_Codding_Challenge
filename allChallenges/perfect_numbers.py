limit = 10000

def isPerfect(num):
    perfect = 0
    for x in range(1, num):
        if num % x == 0:
            perfect += x
    return perfect == num

for num in range(1, limit):
    if isPerfect(num):
        print(str(num), end=', ')
