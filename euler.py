def factorial(value):
    x= 1
    for n in range(value):
        x= x * (n+1)
    return x

print(factorial(0))
print(factorial(5))
print(factorial(8))

def euler_from_series(precision):
    e = 0
    for n in range(precision+1):
        e = e + (1/factorial(n))
    return e

print(euler_from_series(100))