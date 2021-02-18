"""
fibonacci is the summ of previous two

"""

def  fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number -1) + fibonacci(number -2)

for i in range(0, 20):
    print(fibonacci(i), end=" ")


