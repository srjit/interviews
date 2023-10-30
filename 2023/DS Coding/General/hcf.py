# from functools import reduce

# def hcf(l: list) -> int :

#     factors = []
#     limit = reduce(lambda x, y: x * y, l)
#     for i in range(limit, max(l)-1, -1):
#         isfactor = True
#         for j in l:
#             if i % j != 0:
#                 isfactor = False

#         if isfactor:
#             factors.append(i)
        
#     return factors[-1]


# print(hcf([1, 2, 3, 4, 5]))
            
# # 
    
    





# from functools import reduce

# def smallest_multiple(target):
  
#   l = list(range(1, target+1))
  
#   factors = []
#   limit = reduce(lambda x, y: x * y, l)
#   for i in range(limit, max(l)-1, -1):
#     isfactor = True
#     for j in l:
#       if i % j != 0:
#         isfactor = False

#     if isfactor:
#       factors.append(i)
        
#   return factors[-1]


# smallest_multiple(5)




import math

def find_hcf(numbers):
    if len(numbers) < 2:
        return None  # Cannot find HCF for less than two numbers

    hcf_result = numbers[0]
    for num in numbers[1:]:
        hcf_result = math.gcd(hcf_result, num)
    
    return hcf_result


print(find_hcf(list(range(6))))
