from typing import List

def searchInsert(nums: List[int], target: int, startIndex:int=0) -> int:

    limit = len(nums)
    mid = int(limit / 2)

    if limit == 0:
        return startIndex
    if target == nums[mid]:
        return startIndex+mid
    elif target < nums[mid]:
        return searchInsert(nums[:mid], target, startIndex)
    else:
        return searchInsert(nums[mid + 1:], target, startIndex + mid + 1)



print(searchInsert([1,3,5,6], 4))



#
#   Binary Search without recursion 
#


def searchInsert2(nums: List[int], target: int) -> int:

    low, high = 0, len(nums)

    while low < high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
