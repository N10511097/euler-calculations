def factorial(value):
    x= 1
    for n in (range(value)):
        x= x * (n+1)
    return x

print(factorial(0))
print(factorial(5))
print(factorial(8))