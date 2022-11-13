# time complexity: O(nlogn)
# space complexity: O(1)
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        x = len(nums)-1
        for i in range(len(nums)//2):
            max_sum = max(max_sum, nums[i]+nums[x])
            x -= 1
        return max_sum
