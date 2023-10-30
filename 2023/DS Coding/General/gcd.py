



def gcd(a, b):

    while b:
        a, b = b, a % b
    return a

def lcm(a,b):

    return (a*b) / gcd(a, b)



# print(gcd(2, 5))
# print(gcd(9, 18))

# print(lcm(3, 9))
# print(lcm(6, 5))


def lcms(l):

    lcm_ = 1
    for i in l:
        lcm_ = lcm(lcm_, i)

    print(lcm_)


print(lcms([1,2,3,4,5]))
