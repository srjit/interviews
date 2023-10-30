from collections import Counter
# Mean, Median , Mode

def mean(l : list) -> float:

    return sum(l)/len(l)

def median(l: list) -> float:

    l = sorted(l)
    size = len(l)
    if  size % 2 != 0:
        return l[size/2]
    return (l[size/2] + l[(size+1)/2])/2


def mode(l: list) -> float:

    d_ = dict(Counter(l))
    d_sorted = sorted(d_.keys(), reverse=True)
    return d_sorted


print(mode([1,1,2,3,5,2,1,7,3,1]))











    