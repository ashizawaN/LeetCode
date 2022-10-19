from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            nums[index] *= nums[index]
        nums.sort()
        return nums
