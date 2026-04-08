def factorial(n,fact):
    if n==0:
        return fact
    return factorial(n-1,fact*n)
n=int(input('Enter a size: '))
print(factorial(n,1))