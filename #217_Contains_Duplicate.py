from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        x = set()
        for index in range(len(nums)):
            if nums[index] in x:
                return True
            x.add(nums[index])
        return False
        