import math

def mean(x: list) -> float:
    return sum(x)/len(x)


def std(x: list) -> float:
    x_mean = mean(x)
    return math.sqrt(sum([(xi - x_mean)**2 for xi in x]) / len(x))


def cov(x : list, y: list) -> float:

    if len(x) != len(y):
        raise ValueError("Lists must be of equal length")

    x_mean = mean(x)
    y_mean = mean(y)

    return sum([(xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)]) / (len(x) - 1)



def corr(x:list, y:list) -> float:

    if len(x) != len(y):
        raise ValueError("Lists must be of equal length")

    cov_xy = cov(x, y)
    std_x = std(x)
    std_y = std(y)

    return cov_xy / (std_x * std_y)


l1 = [1,2,3,4,5]
l2  = [1,2,3,4,5]

print(corr(l1, l2))



