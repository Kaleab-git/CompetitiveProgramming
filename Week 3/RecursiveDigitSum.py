def add_digits(n):
    sum = 0
    for i in n:
        sum += int(i)
    return str(sum)
def add_digits(n):
    sum = 0
    for i in n:
        sum += int(i)
    return str(sum)

def superDigit2(n, k=1):
    n *= k 
    while len(n) != 1:
        n = add_digits(str(n))
    return n