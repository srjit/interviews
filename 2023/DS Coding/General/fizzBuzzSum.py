

def get_multiples_three(limit):
    '''
    Returns a list of all multiples of 3
    '''
    
    return list(range(3, limit, 3))

def get_multiples_five(limit):
    '''
    Returns a list of all multiples of 5
    '''

    return list(range(5, limit, 5))

def fizz_buzz_sum(target):
    '''
    Returns the sum of all numbers from 1 to target
    that are divisible by 3 or 5
    '''
    
    return sum(set(get_multiples_three(target)
            + get_multiples_five(target)))


print(fizz_buzz_sum(10))
print(fizz_buzz_sum(16))
print(fizz_buzz_sum(100))