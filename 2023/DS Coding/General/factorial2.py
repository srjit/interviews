
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def trailing_zeros(n):

    f = factorial(n)
    
    l = list(str(f))
    count = 0

    i = len(l) - 1
    while l[i] == '0':
        count += 1
        i -= 1
    return count



print(trailing_zeros(30))


