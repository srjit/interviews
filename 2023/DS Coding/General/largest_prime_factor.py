


import math
def remove_biggest_even_factor(target):

    while target % 2 == 0:
        target /= 2
    return target

def largest_prime_factor(target):

    target = remove_biggest_even_factor(target)
    for i in range(target-1, 3, -1):
        
