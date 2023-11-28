from collections import Counter

class Solution:
 
    def removeDuplicates(self, nums: list[int]) -> int:

        nums = list(dict(Counter(nums)).keys())
        k = len(nums)
        print(nums)
        return k
 

s = Solution()
print(s.removeDuplicates([1,1,2]))