def divide(dividend: int, divisor: int) -> int:

    sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1

    _dividend = abs(dividend)
    _divisor = abs(divisor)

    count = _divisor
    i = 1 
    while count <= _dividend:
        count += _divisor
        i += 1

    op = i-1
    if sign == -1:
        op = 0 - op

    return op        



print(divide(-10, -3))