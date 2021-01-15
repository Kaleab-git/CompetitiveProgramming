def factorial(n):
    if n < 0:
        return 'undefined'
    if n==1 or n==0:
        return 1
    else:
        return (factorial(n-1)*n)