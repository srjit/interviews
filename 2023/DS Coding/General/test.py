




def gcd(a, b):

    while b:
        a, b = b, a % b
    return a

def lcm(a,b):

    return (a*b) / gcd(a, b)


def smallest_multiple(target):

    l = list(range(1, target+1))

    lcm_ = 1
    for i in l:
        lcm_ = lcm(lcm_, i)
        
    return lcm_

print(smallest_multiple(5))