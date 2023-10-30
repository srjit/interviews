


# def two_sum(input: list[int], target: int) -> list[int]:

#     for i, num in enumerate(input):
#         partner = target - num
#         if partner in input and partner != num:
#             return [i, input.index(partner)]
#     return [-1, -1]
        

# def two_sum(input: list[int], target: int) -> list[int]:

#     partners = [[idx, input.index(target - i)] for idx, i in enumerate(input) if i != target-i and target-i in input]
#     partners = partners[0] if len(partners) > 0 else [-1, -1]

#     return partners


def two_sum(input: list[int], target: int) -> list[int]:

    d = {i: idx for idx, i in enumerate(input)}

    for idx, i in enumerate(input):
        partner = target - i
        if partner in d and partner != i:
            return [idx, d[partner]]
    return [-1,-1]


    # d = {}
    # for idx, i in enumerate(input):
    #     complement = target - i
    #     if complement in d:
    #         return [idx, d[complement]]
    #     d[i] = idx
    # return [-1, -1]




print(two_sum([1, 4, 6, 10], target = 2))
print(two_sum([1, 4, 6, 10], target = 10))
print(two_sum([1, 4, 6, 10], target = 2))
